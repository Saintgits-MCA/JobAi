from datetime import date
import openai
from django.db import connection
from django.shortcuts import get_object_or_404, render, redirect
import os
import re
import json
from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
import tempfile
# from weasyprint import HTML
from docx import Document
from django.conf import settings
from .models import *
from django.contrib import messages


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
            messages.success(request, "Login Successfully")
            return redirect('home')  # Redirect to a dashboard or home page after login
        except Jobseeker_Registration.DoesNotExist:
            messages.error(request, "Invalid Email or Password")
    return render(request, 'jobseeker_login.html')


def jobseeker_home(request):
    content = ""
    alert_message = ""
    fname = ''
    jobseek_email = ""
    jobseek_loc = ""
    jphone = ""
    jdob = ""
    jskills = ""
    jeducation = ""
    juniversity = ""
    fname = request.session.get('jobseeker_name')
    jobseek_email = request.session.get('jobseeker_email')
    extracted_details = None
    if request.method == "POST":
        uploaded_file = request.FILES.get("word_file")
        resume = request.POST.get("word_file")
        jobseeker_resumeobj = jobseeker_resume()
        jobseeker_resumeobj.resume = resume
        jobseeker_resumeobj.save()
        if uploaded_file:
            # Validate file extension
            if not uploaded_file.name.lower().endswith(('.doc', '.docx')) and not uploaded_file.name.lower().contains("Resume", "CV"):
                return JsonResponse({"error": "Only Resumes with .doc and .docx files are allowed."}, status=400)
                return redirect("jobseeker_home")
            try:
                # Ensure media directories exist
                documents_dir = os.path.join(settings.MEDIA_ROOT, "documents")
                json_dir = os.path.join(settings.MEDIA_ROOT, "json")
                os.makedirs(documents_dir, exist_ok=True)
                os.makedirs(json_dir, exist_ok=True)
                
                # Save the uploaded file
                fs = FileSystemStorage(location=documents_dir)
                file_path = fs.save(uploaded_file.name, uploaded_file)
                file_path = fs.path(file_path)
                
                # Read the Word document content
                document = Document(file_path)
                paragraphs = [p.text for p in document.paragraphs if p.text.strip()]
                content = "\n".join(paragraphs)
               
                # Extract resume details
                extracted_details = extract_resume_details(content)
                # resume_details = ResumeDetails.objects.create(**extracted_details)
                jid = request.session.get('jobseeker_id')
                jobseekerdt = jobseeker_profile.objects.get(user=jid)
                jobseek_loc = jobseekerdt.address
                jphone = jobseekerdt.phone
                jdob = jobseekerdt.dob
                jskills = jobseekerdt.skills
                jeducation = jobseekerdt.highest_qualification
                juniversity = jobseekerdt.university

                # Check if essential details are missing
                if not extracted_details.get("name") or not extracted_details.get("email") or not extracted_details.get("phone"):
                    alert_message = "*Failed to extract your resume.Check your file and try again."
                    jobseeker_resumeobj.delete()
                else:
                    # Convert document to JSON and save
                    json_data = convert_docx_to_json(file_path, uploaded_file.name)
                    messages.success(request, "Resume uploaded successfully!")                    
            except Exception as e: 
                messages.error(request, f"Error reading document: {str(e)}")
            except jobseeker_profile.DoesNotExist:
                messages.error(request, "Profile not found. Please complete your profile.")
                return redirect('home')  # Redirect to a profile creation view
       
    context = {
        "resume_details": extracted_details,
        "alert_message": alert_message,
        "fname":fname,
        "email":jobseek_email,
        "address":jobseek_loc,
        "phone":jphone,
        "dob":jdob,
        "skills":jskills,
        "university":juniversity,
        "education":jeducation
        
    }   
    return render(request, "jobseeker_home.html", context)


def jobseeker_profile_update(request):
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
        job_preference = request.POST.get('job_preferences')
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
            jobseeker_obj.save()
            messages.success(request, "Updated profile auccessfully")
    return redirect('home')


def main(request):
    return render(request, 'index.html')


def base(request):
    return render(request, 'base.html')


def Register(request):
    name = ""
    email = ""
    password = ""
    if request.method == "POST": 
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if Jobseeker_Registration.objects.filter(name=name).exists() or Jobseeker_Registration.objects.filter(email=email).exists():
            messages.error(request, "A Jobseeker with this name and/or email already exists.You can Login directly.")
        else:
            jobseeker_obj = Jobseeker_Registration()
            jobseeker_obj.name = name
            jobseeker_obj.email = email
            jobseeker_obj.password = password
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
    jobs = company_joblist.objects.all()  # Fetch all jobs from the database
    return render(request, 'search-job.html', {"fname":fname, 'jobs': jobs})


def coverletter(request):
    company = Company.objects.all()
    fname = request.session.get('jobseeker_name')
    email = request.session.get('jobseeker_email')
    openai.api_key = settings.OPENAI_API_KEY

    if request.method == "POST":
        # Get form data
        name = request.POST.get("name", "Your Name")
        position = request.POST.get("position", "Job Title")
        company_id = request.POST.get("Companyname", "Company Name")
        hr_name = request.POST.get("hrname", "Hiring Manager")
        skills = request.POST.get("skills", "Your Skills")
        job_type = request.POST.get("jobtype", "Job Type")
        phone = request.POST.get("phone", "Phone Number")
        ldate=date.today().strftime('%d-%m-%Y')
        try:
            company_obj = Company.objects.get(id=company_id)
            company_name = company_obj.name
            company_loc=company_obj.address
        except Company.DoesNotExist:
            company_name = "Unknown Company"

        # OpenAI API Call for Cover Letter Generation
        prompt = f"""
        Write a professional cover letter for fresher jobseeker named {name} with {email} and {phone} for getting a {job_type} job in a {position} role at {company_name} whose address is {company_loc}. 
        send letter with company address to {hr_name}, mention skills like {skills} with date of {ldate}, and make it engaging and brief without blocks like '[ ]' instead give values provided.
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
            "company": company
        })

    return render(request, "cover-letter.html", {
        "fname": fname,
        "company": company,
        "email": email
    })


def settings_view(request):
    fname = request.session.get('jobseeker_name')
    jobseek_email = request.session.get('jobseeker_email')  
    return render(request, 'settings_view.html', {"fname":fname, "email":jobseek_email})


def support(request):
    fname = request.session.get('jobseeker_name')
    return render(request, 'support.html', {"fname":fname})


def mockinterview(request):
    fname = request.session.get('jobseeker_name')
    return render(request, 'mock-interview.html', {"fname":fname})


def autoapply(request):
    fname = request.session.get('jobseeker_name')
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
    
    if request.method == "POST": 
        job_id = request.POST.get("job_id")
        messages.success(request, f"jobid:{str(job_id)}")
        if not job_id:
            messages.error(request, "Job ID is missing in request.")
            return render(request, 'company_jobs.html', {'cname': cname})
        
        try:
            job = get_object_or_404(company_joblist, id=job_id)
            job.delete()
            messages.success(request, "Job deleted successfully")
            return redirect('job_listing')
        except Exception as e:
            messages.error(request, f"Error deleting job: {str(e)}")
    else: 
        messages.error(request, "Attempt for deleting job item failed")
        
    return render(request, 'company_jobs.html', {'cname': cname})


def company_type(request):
    if request.method == "POST":
        company_type = request.POST.get('ctype')
        company_typeobj = Company_Type_Master()
        company_typeobj.company_type = company_type
        company_typeobj.save()
        messages.success(request, "Company type registered successfully!")
        return render(request, 'company_type.html')
    return render(request, 'company_type.html')

    
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
            return render(request, 'company_jobs.html', {"cname": cname})
        
        # Get expired jobs
        expiredyet = company_joblist.objects.filter(company_id=cid, Lastdate__gt=date.today())
        count = company_joblist.objects.filter(company=cid).count()  # Count jobs for the logged-in company
        context = {
            "jobs": expiredyet,
            "cname": cname,
            "count":count
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
                "job_title": job.job_title,
                "job_description": job.job_description,
                "eligibility": job.highest_qualification,
                "skills": job.skills_required,
                "location": job.location,
                "job_type": job.job_type,
                "last_date": job.Lastdate,
                "list_date": job.dateofpublish,
            }
            jobs_list.append(job_info)
        
        # Get expired jobs
        expiredyet = company_joblist.objects.filter(company=cid, Lastdate__gt=date.today())
        
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
    cid = request.session.get('company_id')
    if request.method == "POST":
        job_number = request.POST.get('job_number')
        job_title = request.POST.get('job_title')
        job_description = request.POST.get('job_description')
        job_location = request.POST.get('Location')
        job_type = request.POST.get('Job_type')
        jobposted_date = request.POST.get('jobposted_date')
        qualification = request.POST._getlist('highest_qualification')
        skills = request.POST._getlist('skills_required')
        lastdate = request.POST.get('deadline')
        if company_joblist.objects.filter(job_number=job_number).exists():
            messages.error(request, "A job with this job number already posted in this portal use other id to post other jobs")
        else:
            companyjob_obj = company_joblist()
            companyjob_obj.company_id = cid
            companyjob_obj.job_number = job_number
            companyjob_obj.job_title = job_title
            companyjob_obj.job_description = job_description
            companyjob_obj.location = job_location
            companyjob_obj.job_type = job_type
            companyjob_obj.dateofpublish = jobposted_date
            companyjob_obj.highest_qualification = qualification
            companyjob_obj.skills_required = skills
            companyjob_obj.Lastdate = lastdate
            companyjob_obj.save()
            messages.success(request, "Job Posted Successfully!!") 
    cname = request.session.get('company_name')
    return render(request, 'company_postjob.html', {"cname":cname, 'cdate':date.today().strftime("%Y-%m-%d")})


def edit_job(request):
    cname = request.session.get('company_name')
    return render(request, 'edit-job.html', {"cname":cname})


def download_pdf(request):
    cover_letter_text = request.GET.get("cover_letter", "No cover letter provided.")

    # Render the HTML template as a string
    html_string = render_to_string("cover-letter.html", {"cover_letter": cover_letter_text})

    # Create a temporary file for PDF output
    with tempfile.NamedTemporaryFile(delete=True) as temp_pdf:
        # HTML(string=html_string.encode("utf-8")).write_pdf(temp_pdf.name)
        temp_pdf.seek(0)  # Move file pointer to the beginning
        pdf_content = temp_pdf.read()

    # Return the generated PDF as a response
    response = HttpResponse(pdf_content, content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="cover_letter.pdf"'

    return response
