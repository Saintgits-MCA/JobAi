from datetime import date
import openai
from django.db import connection
from django.shortcuts import get_object_or_404, render, redirect
import os
import re
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage
# from weasyprint import HTML
from docx import Document
from django.conf import settings
from .models import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

openai.api_key = settings.OPENAI_API_KEY

def extract_resume_details(content):
    """Extracts key details like name, skills, address, highest_qualification, job_preference, university name, date of birth, email, and phone number from the resume content."""
    details = {
        "name": "",
        "skills": "",
        "address": "",
        "highest_qualification": "",
        "job_preference": "",
        "university": "",
        "dob": "",
        "email": "",
        "phone": ""
    }
    
    email_pattern = r"[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+"
    phone_pattern = r"\+?\d{10,15}"
    dob_pattern = r"\b(\d{1,2}[-/ ](?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-/ ]\d{2,4}|\d{1,2}[-/]\d{1,2}[-/]\d{2,4})\b"
    qualification_keywords = ["Bachelor's Degree", "MCA", "Master of Computer Application", "PhD", "B.Sc", "M.Sc", "B.Tech Computer Science", "M.Tech Computer Science", "MBA"]
    job_preferences_keywords = ["Software Engineer", "Data Scientist", "Backend Developer", "Frontend Developer", "Project Manager"]
    university_keywords = ["University", "Institute", "College"]
    skills_keywords = ["Python", "Java", "C++", "Django", "SQL", "Machine Learning", "Artificial Intelligence", "React", "JavaScript", "HTML", "CSS", "Git"]
    address_keywords = ["State", "Country", "District"]
    indian_states = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]
    
    resume_data = {}  # Dictionary to store extracted details
    
    lines = content.split("\n")
    for line in lines:
        line = line.strip()
        
        if not details["name"] and re.match(r"^[A-Z][a-z]+\s[A-Z][a-z]+", line):
            details["name"] = line
        
        if not details["email"] and re.search(email_pattern, line):
            details["email"] = re.search(email_pattern, line).group()
        
        if not details["phone"] and re.search(phone_pattern, line):
            details["phone"] = re.search(phone_pattern, line).group()
        
        if not details["dob"] and re.search(dob_pattern, line):
            details["dob"] = re.search(dob_pattern, line).group()
        
        if any(keyword.lower() in line.lower() for keyword in address_keywords) or any(state.lower() in line.lower() for state in indian_states):
            details["address"] = line
        
        for qualification in qualification_keywords:
            if qualification.lower() in line.lower():
                details["highest_qualification"] = qualification
                break
                
        for job in job_preferences_keywords:
            if job.lower() in line.lower():
                details["job_preference"] = job
                break
                
        for university in university_keywords:
            if university.lower() in line.lower():
                details["university"] = line
                break
                
        for skill in skills_keywords:
            if skill.lower() in line.lower():
                details["skills"] += skill + ", "
    
    details["skills"] = details["skills"].rstrip(", ")
    resume_data.update(details)  # Storing extracted details in the list
    
    return details


def convert_docx_to_json(docx_path, filename):
    """Convert a .docx file to JSON format and save it to media folder"""
    document = Document(docx_path)
    data = {"paragraphs": []}

    for para in document.paragraphs:
        data["paragraphs"].append(para.text)
    
    json_path = os.path.join(settings.MEDIA_ROOT, "json", filename + ".json")
    
    try:
        with open(json_path, "w") as json_file:
            json.dump(data, json_file, indent=4)
    except Exception as e:
        print(f"Error saving JSON file: {e}")
    
    return json.dumps(data, indent=4)
# Create your views here.


def jobseeker_login(request):
    if request.method == "POST":
        Email = request.POST.get("email")
        Password = request.POST.get("password")
        try:
            jobseeker = Jobseeker_Registration.objects.get(email=Email, password=Password)
            request.session['jobseeker_name'] = jobseeker.name
            request.session['jobseeker_id'] = jobseeker.id
            request.session['jobseeker_email'] = jobseeker.email
            request.session['jobseeker_phone'] = jobseeker.phone
            messages.success(request, "Login Successfully")
            return redirect('jobseeker_dashboard')  # Redirect to a dashboard or home page after login
        except Jobseeker_Registration.DoesNotExist:
            messages.error(request, "Invalid Email or Password")
    return render(request, 'jobseeker_login.html')


def jobseeker_home(request):
    content = ""
    alert_message = ""
    fname = request.session.get('jobseeker_name')
    uid = request.session.get('jobseeker_id')
    jobseek_email = request.session.get('jobseeker_email')
    phone = request.session.get('jobseeker_phone')
    extracted_details = None
    show_modal=False
    if request.method == "POST":
        uploaded_file = request.FILES.get("word_file")

        # Check if a resume already exists for the user
        if jobseeker_resume.objects.filter(user_id=uid).exists():
            messages.error(request, "You have already uploaded a resume. You cannot upload another one.")
            return redirect("home")

        if uploaded_file:
            # Validate file extension before saving
            allowed_extensions = ('.doc', '.docx')
            file_extension = os.path.splitext(uploaded_file.name)[1].lower()
            
            if file_extension not in allowed_extensions:
                messages.error(request, "Invalid file format. Only .doc and .docx files are allowed. PDFs are not accepted.")
                return redirect("home")  # Prevents further execution

            try:
                jobseeker_profile.objects.get(user_id=uid)
            except jobseeker_profile.DoesNotExist:
                show_modal = True  # Show modal if profile does not exist

                # Ensure media directories exist
                documents_dir = os.path.join(settings.MEDIA_ROOT, "documents")
                json_dir = os.path.join(settings.MEDIA_ROOT, "json")
                os.makedirs(documents_dir, exist_ok=True)
                os.makedirs(json_dir, exist_ok=True)

                # Save the uploaded file (only after validation)
                fs = FileSystemStorage(location=documents_dir)
                file_path = fs.save(uploaded_file.name, uploaded_file)
                file_path = fs.path(file_path)

                # Read the Word document content
                document = Document(file_path)
                paragraphs = [p.text for p in document.paragraphs if p.text.strip()]
                content = "\n".join(paragraphs)

                # Extract resume details
                extracted_details = extract_resume_details(content)

                # Check if essential details are missing
                if not extracted_details.get("name") or not extracted_details.get("email") or not extracted_details.get("phone"):
                    messages.error(request, "Failed to extract essential details from your resume. Check your file and try again.")
                    # Delete the saved file if details are not extracted
                    os.remove(file_path)
                    return redirect("home")

                # Save the resume in the database only after successful validation
                jobseeker_resumeobj = jobseeker_resume(file=uploaded_file, user_id=uid)
                jobseeker_resumeobj.save()

                # messages.success(request, "Resume uploaded successfully!")

            except Exception as e:
                messages.error(request, f"Error reading document: {str(e)}")

    context = {
        "resume_details": extracted_details,
        "alert_message": alert_message,
        "fname": fname,
        "email": jobseek_email,
        "phone": phone,
        "show_modal":show_modal
    }
    if not jobseeker_profile.objects.filter(name=fname).exists() and not jobseeker_resume.objects.filter(user=uid):
        messages.error(request, "Complete this Profile Registration and enjoy all features of this portal")
        redirect('home')
    return render(request, "jobseeker_home.html", context)


def jobseeker_profile_update(request):
    userid=request.session.get('jobseeker_id')
    dob = ""
    phone = ""
    address = ""
    qualification = ""
    skills = ""
    job_preference = ""
    if request.method == "POST": 
        name = request.POST.get('name')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        phone = request.POST.get('phone')
        address = request.POST.get('Address')
        qualification = request.POST.get('Education')
        university = request.POST.get('University')
        skills = request.POST.get('skills')
        image=request.FILES.get('image')
        job_preference = request.POST.get('job_preferences')
        # Fetch the first resume for the user (if multiple exist)
        resume = jobseeker_resume.objects.filter(user=userid).first()
        cv = resume.file if resume else None  # Handle case where no resume exists
        
        if jobseeker_profile.objects.filter(name=name).exists() and jobseeker_profile.objects.filter(email=email).exists():
            messages.error(request, "A Jobseeker with this name and/or email already exists. Please use different details.")
        else:
            jobseeker_obj = jobseeker_profile()
            jobseeker_obj.name = name
            jobseeker_obj.email = email
            jobseeker_obj.dob = dob
            jobseeker_obj.highest_qualification = qualification
            jobseeker_obj.skills = skills
            jobseeker_obj.job_preference = job_preference
            jobseeker_obj.university = university
            jobseeker_obj.address = address
            jobseeker_obj.phone = phone
            jobseeker_obj.profile_img=image
            jobseeker_obj.user_id=userid
            jobseeker_obj.resume=cv
            jobseeker_obj.save()
            request.session['address']=jobseeker_obj.address
            request.session['dob']=jobseeker_obj.dob
            messages.success(request, "Updated profile successfully.Now you can use whole features of this portal.")
    return redirect('home')


def main(request):
    return render(request, 'index.html')


def base(request):
    jbid=request.session.get('jobseeker_id')
    if jobseeker_profile.objects.filter(user=jbid).exists():
        jobseeker=jobseeker_profile.objects.get(user=jbid)
        return render(request,'base.html',jobseeker)
    else:
        jobseeker=None
    return render(request, 'base.html',jobseeker)


def Register(request):
    name = ""
    email = ""
    password = ""
    if request.method == "POST": 
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone=request.POST.get('Phone')
        if Jobseeker_Registration.objects.filter(name=name).exists() or Jobseeker_Registration.objects.filter(email=email).exists():
            messages.error(request, "A Jobseeker with this name and/or email already exists.You can Login directly.")
        else:
            jobseeker_obj = Jobseeker_Registration()
            jobseeker_obj.name = name
            jobseeker_obj.email = email
            jobseeker_obj.password = password
            jobseeker_obj.phone=phone
            jobseeker_obj.save()
            messages.success(request, "Jobseeker registered successfully!.Email will be your Username")
            return render(request, 'jobseeker_register.html')
    return render(request, 'jobseeker_register.html')


def Forgot_pwd(request):
    return render(request, 'forgot-password.html')


def user_base(request):
    return render(request, 'base.html')


def jobseeker_logout(request):
    logout(request)
    request.session.clear()
    return render(request, 'jobseeker_login.html')


def company_logout(request):
    logout(request)
    request.session.clear()
    return render(request, 'company_login.html')


def search_job(request):
    fname = request.session.get('jobseeker_name')
    if not jobseeker_profile.objects.filter(name=fname).exists():
            return redirect('home')
    jobs = company_joblist.objects.all()  # Fetch all jobs from the database
    return render(request, 'search-job.html', {"fname":fname, 'jobs': jobs})


def coverletter(request):
    job=job_title.objects.all()
    company = Company.objects.all()
    fname = request.session.get('jobseeker_name')
    email = request.session.get('jobseeker_email')
    phoneno=request.session.get('jobseeker_phone')
    if not jobseeker_profile.objects.filter(name=fname).exists():
        return redirect('home')
    

    if request.method == "POST":
        # Get form data
        name = request.POST.get("name", "Your Name")
        position = request.POST.get("job_title", "Job Title")
        company_id = request.POST.get("Companyname", "Company Name")
        hr_name = request.POST.get("hrname", "Hiring Manager")
        skills = request.POST.get("skills", "Your Skills")
        job_type = request.POST.get("jobtype", "Job Type")
        phone = request.POST.get("phone", "Phone Number")
        address=request.POST.get("Address")
        eligibility=request.POST.get('eligibility')
        ldate=date.today().strftime('%d-%m-%Y')
        try:
            company_obj = Company.objects.get(id=company_id)
            company_name = company_obj.name
            company_loc=company_obj.address
            job_position=job_title.objects.get(id=position)
            jobs=job_position.job_title
        except Company.DoesNotExist:
            company_name = "Unknown Company"

        # OpenAI API Call for Cover Letter Generation
        prompt = f"""
Write a professional and engaging cover letter for a fresher job seeker named {name} , whose address is {address} ,email is {email},having qualification of '{eligibility}' and phone number is {phone}. 
The job seeker is applying for a {job_type} position as {jobs} at {company_name}, located at {company_loc}. 

Address the letter to {hr_name}, incorporating the company's full address. Highlight relevant skills such as {skills} and ensure the letter is formatted in a common professional style without placeholders like [Your Name] or [Your Address]. 

Include the date ({ldate}) at the beginning and conclude with a proper closing, using the candidate’s full name instead of placeholders. Keep the letter concise, engaging, and directly relevant to the job opportunity.
"""
        
        response = openai.ChatCompletion.create(
             model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": prompt}
  ]
        )

        cover_letter = response["choices"][0]["message"]["content"].strip()

        return render(request, "cover-letter.html", {
            "fname": fname,
            "email": email,
            "cover_letter": cover_letter,
            "company": company,
            "phone":phoneno,
            "job":job
        })
    jsdt=jobseeker_profile.objects.get(email=email)
    return render(request, "cover-letter.html", {
        "fname": fname,
        "company": company,
        "email": email,
        "phone":phoneno,
        "job":job,
        "jsdt":jsdt
    })


def settings_view(request):    
    jbid=request.session.get('jobseeker_id')
    try: 
        jsdt=jobseeker_profile.objects.get(user_id=jbid)
        fname = request.session.get('jobseeker_name')
        jobseek_email = request.session.get('jobseeker_email') 
        phone=request.session.get('jobseeker_phone')
        # address=request.session.get("address")
        context = {
            'jsdt':jsdt,
                "fname":fname,
                "email":jobseek_email,
                "phone":phone,
            }
        return render(request, 'settings_view.html', context)
    except:
        
        jsdt=Jobseeker_Registration.objects.filter(id=jbid)
        fname = request.session.get('jobseeker_name')
        if not jobseeker_profile.objects.filter(name=fname).exists():
            return redirect('home')
        context = {
            'jsdt':jsdt,
                "fname":fname,
              
            }
        return render(request,'settings_view.html', context)
        


def support(request):
    fname = request.session.get('jobseeker_name')
    if not jobseeker_profile.objects.filter(name=fname).exists():
            return redirect('home')
    return render(request, 'support.html', {"fname":fname})


def mockinterview(request):
    fname = request.session.get('jobseeker_name')
    if not jobseeker_profile.objects.filter(name=fname).exists():
            return redirect('home')
    jobs=job_title.objects.all()
    if request.method == "POST":
        job_id = request.POST.get("job_title")
        user_answer = request.POST.get("answer", None)

        if not job_id:
            return JsonResponse({"error": "Job title is required"}, status=400)

        try:
            job = job_title.objects.get(id=job_id)
        except job_title.DoesNotExist:
            return JsonResponse({"error": "Invalid job title"}, status=400)

        if user_answer is None:
            # Generate exactly 5 interview questions for the given job title
            prompt = f"Provide exactly 5 professional interview questions for a {job.job_title} role. Do not include any introduction or explanation. List them one after another."
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role": "system", "content": prompt}]
            )

            questions = response["choices"][0]["message"]["content"].strip().split("\n")
            return JsonResponse({"questions": questions})

        else:
            # Evaluate the user answer
            prompt = f"Evaluate this job interview response for a {job.job_title} role and provide constructive feedback. Do not include any introduction or pleasantries. Answer concisely.\n\nAnswer: {user_answer}"
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role": "system", "content": prompt}]
            )
            feedback = response["choices"][0]["message"]["content"].strip()
            return JsonResponse({"feedback": feedback})

    return render(request, 'mock-interview.html', {'job': jobs,"fname":fname})


def autoapply(request):
    fname = request.session.get('jobseeker_name')
    if not jobseeker_profile.objects.filter(name=fname).exists():
        return redirect('home')
    return render(request, 'auto-apply.html', {"fname":fname})


def user_type(request):
    return render(request, 'user-type.html')


def company_login(request):
    if request.method == "POST":
        Email = request.POST.get("email")
        Password = request.POST.get("password")
        try: 
            company = Company.objects.get(email=Email, password=Password) 
            request.session['company_id'] = company.id
            request.session['company_name'] = company.name
            request.session['company_email'] = company.email
            # request.session['company_address']=company.address
            # request.session['company_type']=company.company_type_id
            messages.success(request, "Login Successfully")
            return redirect('company_dashboard')  # Redirect to a dashboard or home page after login
        except Company.DoesNotExist:
            messages.error(request, "Invalid Email or Password")
    return render(request, 'company_login.html')


def company_registration(request):
    if request.method == "POST":
        name = request.POST.get('company_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        company_type = request.POST.get("CompanyType")  # This returns a string
        company_address = request.POST.get('Address')
        # Check if a company with the same name or email already exists
        if Company.objects.filter(name=name).exists() or Company.objects.filter(email=email).exists():
            messages.error(request, "A company with this name or email already exists. You can Login.")
        else:
            # Create and save the company
            companyobj = Company()
            companyobj.name = name
            companyobj.password = password
            companyobj.email = email
            companyobj.company_type_id = company_type
            companyobj.address = company_address
            companyobj.save()
            messages.success(request, "Company registered successfully!.Email will be your Username")
            return redirect('company_registration')
    company = Company_Type_Master.objects.all()
    context = {
        'company':company
    }
    return render(request, 'company_registration.html', context)


def delete_job(request): 
    cname = request.session.get('company_name')
    job_id = request.GET.get("ids")
    messages.success(request, f"jobid:{str(job_id)}")
    if not job_id:
            messages.error(request, "Job ID is missing in request.")
            return render(request, 'company_jobs.html', {'cname': cname})
        
    try:
            job = get_object_or_404(company_joblist, id=job_id)
            job.delete()
            # Reset auto-increment (adjust for your database)
            with connection.cursor() as cursor:
                cursor.execute("ALTER TABLE jobai1.jobai_app_company_joblist AUTO_INCREMENT = 1")
            messages.success(request, "Job deleted successfully")
            return redirect('job_listing')
    except Exception as e:
            messages.error(request, f"Error deleting job: {str(e)}")
    else: 
        messages.error(request, "Attempt for deleting job item failed")
        
    return render(request, 'company_jobs.html', {'cname': cname})

def delete_user_profile(request):
    jid=request.session.get('jobseeker_id')
    user=get_object_or_404(jobseeker_profile, user=jid)
    user.delete()
    resume=get_object_or_404(jobseeker_resume, user=jid)
    resume.delete()
    # Reset auto-increment (adjust for your database)
    with connection.cursor() as cursor:
        cursor.execute("ALTER TABLE jobai1.jobai_app_jobseeker_profile AUTO_INCREMENT = 1")
        cursor.execute("ALTER TABLE jobai1.jobai_app_jobseeker_resume AUTO_INCREMENT = 1")
        messages.success(request, "Profile deleted successfully")
        return redirect('settings_view')
    jsdt=Jobseeker_Registration.objects.get(id=jid)
    fname = request.session.get('jobseeker_name')
    if not jobseeker_profile.objects.filter(name=fname).exists():
        return redirect('home')
    context = {
            'jsdt':jsdt,
                "fname":fname,
              
            }
    return render(request,'settings_view.html', context)

def company_type(request):
    if request.method == "POST":
        company_type = request.POST.get('ctype')
        company_typeobj = Company_Type_Master()
        company_typeobj.company_type = company_type
        company_typeobj.save()
        messages.success(request, "Company type registered successfully!")
        return render(request, 'company_type.html')
    return render(request, 'company_type.html')

def jobs(request):
    if request.method == "POST":
        job_title1 = request.POST.get('job')
        company_typeobj = job_title()
        company_typeobj.job_title = job_title1
        company_typeobj.save()
        messages.success(request, "Job title added successfully!")
        return render(request, 'job_position.html')
    return render(request, 'job_position.html')

    
def company_forgot_password(request):
    return render(request, 'company_forgot_pwd.html')


def company_dashboard(request):
    try:
        cname = request.session.get('company_name')
        cid = request.session.get('company_id')
        
        # Fetch all job listings for the logged-in company
        compjobdt = company_joblist.objects.filter(company=cid)
        # If no jobs exist, show the default page
        if not compjobdt.exists():
            count=0
            return render(request, 'company_dashboard.html', {"cname": cname,"count":count})
        
        # Get expired jobs
        # expiredyet = company_joblist.objects.filter(company_id=cid, Lastdate__gt=date.today())
        count = compjobdt.count()  # Count jobs for the logged-in company
        context = {
            # "jobs": expiredyet,
            "cname": cname,
            "count":count,
        }
        return render(request, 'company_dashboard.html', context)
    except Exception as e:
        # Handle unexpected errors
        return render(request, 'company_dashboard.html', {"cname": cname, "error": str(e)})

    
def company_settings(request):
    cid = request.session.get('company_id')
    # =request.session.get('company_email')
    # ctype=request.session.get('company_type')
    # cloc=request.session.get('company_address')
    compdt = Company.objects.get(id=cid)
    cmail = compdt.email
    cname = compdt.name
    cloc = compdt.address
    ctype = compdt.company_type.company_type
    context = {
        "cname":cname, "cmail":cmail, "cloc":cloc,
        "ctype":ctype
    }
    return render(request, 'company_settings_view.html', context)


def company_jobs(request):
    try:
        cname = request.session.get('company_name')
        cid = request.session.get('company_id')
        
        # Fetch all job listings for the logged-in company
        compjobdt = company_joblist.objects.filter(company=cid)
        # If no jobs exist, show the default page
        if not compjobdt.exists():
            return render(request, 'company_jobs.html', {"cname": cname})
        
        # Iterate through each job for the company
        jobs_list = []
        for job in compjobdt:
            job_info = {
                "job_id": job.id,
                "job_number": job.job_number,
                "job_title": job.job_title.job_title,
                "job_description": job.job_description,
                "eligibility":(job.highest_qualification),
                "skills": job.skills_required,
                "location": job.location,
                "job_type": job.job_type,
                "last_date": job.Lastdate,
                "list_date": job.dateofpublish,
            }
            jobs_list.append(job_info)

        # Get expired jobs
        expiredyet = company_joblist.objects.filter(company=cid, Lastdate__gt=date.today())
        # Convert string to list if stored incorrectly

        context = {
            "jobs": expiredyet,
            "jobs_list": jobs_list,
            "cname": cname,
        }
        return render(request, 'company_jobs.html', context)
    
    except Exception as e:
        # Handle unexpected errors
        return render(request, 'company_jobs.html', {"cname": cname, "error": str(e)})


def company_postjob(request):
    job=job_title.objects.all()
    cid = request.session.get('company_id')
    if request.method == "POST":
        job_number = request.POST.get('job_number')
        job_position = request.POST.get('job_title')
        job_description = request.POST.get('job_description')
        job_location = request.POST.get('Location')
        job_type = request.POST.get('Job_type')
        jobposted_date = request.POST.get('jobposted_date')
        qualification = request.POST.getlist('highest_qualification')
        skills = request.POST.getlist('skills_required')
        qualification_str = ",".join(qualification)
        skills_str = ",".join(skills)
        lastdate = request.POST.get('deadline')
        if company_joblist.objects.filter(job_number=job_number).exists():
            messages.error(request, "A job with this job number already posted in this portal use other id to post other jobs")
        else:
            companyjob_obj = company_joblist()
            companyjob_obj.company_id = cid
            companyjob_obj.job_number = job_number
            companyjob_obj.job_title_id = job_position
            companyjob_obj.job_description = job_description
            companyjob_obj.location = job_location
            companyjob_obj.job_type = job_type
            companyjob_obj.dateofpublish = jobposted_date
            companyjob_obj.highest_qualification = qualification_str
            companyjob_obj.skills_required = skills_str
            companyjob_obj.Lastdate = lastdate
            companyjob_obj.save()
            messages.success(request, "Job Posted Successfully!!")        
    cname = request.session.get('company_name')
    return render(request, 'company_postjob.html', {"cname":cname, 'cdate':date.today().strftime("%Y-%m-%d"),"job":job})


def edit_job(request):
    job=job_title.objects.all()
    cid = request.session.get('company_id')
    cname = request.session.get('company_name')
    if request.method == "POST":
        job_id  = request.POST.get('job_id')
        job_number = request.POST.get('job_number')
        job_position = request.POST.get('job_title')
        job_description = request.POST.get('job_description')
        job_location = request.POST.get('location')
        job_type = request.POST.get('job_type')
        # jobposted_date = request.POST.get('jobposted_date')
        qualification = request.POST.getlist('highest_qualification')
        skills = request.POST.getlist('skills_required')
        qualification_str = ",".join(qualification)
        skills_str = ",".join(skills)
        lastdate = request.POST.get('deadline')
        # if company_joblist.objects.get(job_number=job_number).exists():
        #     messages.error(request, "A job with this job number already posted in this portal use other id to post other jobs")
        # else:
        
        companyjob_obj = company_joblist.objects.get(id=job_id)
        companyjob_obj.company_id = cid
        companyjob_obj.job_number = job_number
        companyjob_obj.job_title_id = job_position
        companyjob_obj.job_description = job_description
        companyjob_obj.location = job_location
        companyjob_obj.job_type = job_type
        companyjob_obj.dateofpublish = date.today().strftime('%Y-%m-%d')
        companyjob_obj.highest_qualification = qualification_str
        companyjob_obj.skills_required = skills_str
        companyjob_obj.Lastdate = lastdate
        companyjob_obj.save()
        messages.success(request, "Job Edited Successfully!!") 
        return redirect('job_listing')
    jobid=request.GET.get('ids')
    jobobg=company_joblist.objects.get(id=jobid)
    context={
        'jobobg':jobobg,
        "cname":cname,
        "job":job
    }
    return render(request, 'edit-job.html',context)

def jobseeker_dashboard(request):
    fname=request.session.get('jobseeker_name')
    if not jobseeker_profile.objects.filter(name=fname).exists():
        return redirect('home')
    ccount=company_joblist.objects.all()
    company=Company.objects.all()
    jcount=ccount.count()
    compcount=company.count()
    return render(request,'jobseeker_dashboard.html',{"fname":fname,"jcount":jcount,"compcount":compcount,"company":company})


