from datetime import date
import openai
# from django.db import connection
from django.shortcuts import get_object_or_404, render, redirect
import os
import json
from django.http import JsonResponse
from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
# from weasyprint import HTML
from docx import Document
from django.conf import settings
from .models import * #noqa
from django.contrib import messages
from django.core.mail import send_mail
from itertools import groupby
from django.core.mail.message import EmailMessage
import tempfile

openai.api_key = settings.OPENAI_API_KEY


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

def extract_resume_details(content):
    """Extracts key details like name, skills, address, highest_qualification, job_preference, university name, date of birth, email, and phone number from the resume content."""
    import re

    details = {
        "name": "",
        "skills": "",
        "address": "",
        "highest_qualification": "",
        "passout_year": "",
        "percentage": "",
        "job_preference": "",
        "university": "",
        "dob": "",
        "email": "",
        "phone": ""
    }
    
    # Define patterns and keywords
    email_pattern = r"[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+"
    phone_pattern = r"\+?\d{10,15}"
    # passout_year_pattern = r"\b(19\d{2}|20\d{2})\b"
    percentage_pattern = r"(\d{1,2}\.\d{1,2}|\d{1,2})%"
    dob_patterns = [
        r"\b(\d{1,2})[-/ ](\d{1,2})[-/ ](\d{2,4})\b",  # Formats like DD/MM/YYYY, DD-MM-YYYY
        r"\b(\d{1,2})[-/ ](Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-/ ](\d{2,4})\b"  # Formats with month names
    ]
    qualification_keywords = ["Bachelor's Degree","Integrated MCA","MCA", "Master of Computer Application", "PhD", "B.Sc", "M.Sc", "B.Tech Computer Science", "M.Tech Computer Science", "MBA"]
    job_preferences_keywords = ["Software Engineer", "Data Scientist", "Backend Developer", "Frontend Developer", "Project Manager"]
    university_keywords = ["University", "Institute", "College"]
    skills_keywords = ["Python", "Java", "C++", "Django", "SQL", "Machine Learning", "Artificial Intelligence", "React", "JavaScript", "HTML", "CSS", "Git", "Data Analytics"]
    address_keywords = ["State", "Country", "District"]
    indian_states = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]
    
    # Use a set for skills to prevent duplicates
    skills_found = set()
    
    # Process content line-by-line
    lines = content.split("\n")
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Extract name: assume first occurrence of two or more capitalized words is the candidate's name
        if not details["name"]:
            name_match = re.match(r"^([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)", line)
            if name_match:
                details["name"] = name_match.group(1)
        
        # Extract email
        if not details["email"]:
            email_match = re.search(email_pattern, line)
            if email_match:
                details["email"] = email_match.group()
        
        # Extract phone
        if not details["phone"]:
            phone_match = re.search(phone_pattern, line)
            if phone_match:
                details["phone"] = phone_match.group()
        
        # # Extract date of birth
        # if not details["dob"]:
        #     dob_match = re.search(dob_patterns, line, flags=re.IGNORECASE)
        #     if dob_match:
        #         details["dob"] = dob_match.group(1)
        # Extract date of birth and format to YYYY-MM-DD (for HTML date input)
        if not details["dob"]:
            for pattern in dob_patterns:
                dob_match = re.search(pattern, line, flags=re.IGNORECASE)
                if dob_match:
                    try:
                        if len(dob_match.groups()) == 3:
                            day, month, year = dob_match.groups()
                            if month.isdigit():
                                formatted_date = f"{int(year):04d}-{int(month):02d}-{int(day):02d}"
                            else:
                                month_num = {
                                    "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", 
                                    "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
                                }.get(month[:3].capitalize(), "")
                                if month_num:
                                    formatted_date = f"{int(year):04d}-{month_num}-{int(day):02d}"
                                else:
                                    continue
                            details["dob"] = formatted_date
                            break
                    except ValueError:
                        continue
        
        # Extract address if line contains address-related keywords or Indian states
        if not details["address"]:
            if any(kw.lower() in line.lower() for kw in address_keywords) or any(state.lower() in line.lower() for state in indian_states):
                details["address"] = line
        
        # Extract highest qualification
        if not details["highest_qualification"]:
            for qualification in qualification_keywords:
                if qualification.lower() in line.lower():
                    details["highest_qualification"] = qualification
                    break
        
        # Extract percentage
        if not details["percentage"]:
            percentage_match = re.search(percentage_pattern, line)
            if percentage_match:
                details["percentage"] = percentage_match.group()
                
        # Extract job preference
        if not details["job_preference"]:
            for job in job_preferences_keywords:
                if job.lower() in line.lower():
                    details["job_preference"] = job
                    break
        
        # Extract university: store the entire line if it contains any keyword
        if not details["university"]:
            for uni_kw in university_keywords:
                if uni_kw.lower() in line.lower():
                    details["university"] = line
                    break
        
        # Accumulate skills from the line
        for skill in skills_keywords:
            if skill.lower() in line.lower():
                skills_found.add(skill)
    
    details["skills"] = ", ".join(sorted(skills_found))
    return details


def jobseeker_home(request):
    content = ""
    alert_message = ""
    fname = request.session.get('jobseeker_name')
    uid = request.session.get('jobseeker_id')
    jobseek_email = request.session.get('jobseeker_email')
    phone = request.session.get('jobseeker_phone')
    extracted_details = None
    show_modal = False

    if request.method == "POST":
        uploaded_file = request.FILES.get("word_file")

        # Check if a resume already exists for the user
        if jobseeker_resume.objects.filter(user_id=uid).exists():
            messages.error(request, "You have already uploaded a resume. You cannot upload another one.")
            return redirect("home")

        if uploaded_file:
            allowed_extensions = ('.doc', '.docx')
            file_extension = os.path.splitext(uploaded_file.name)[1].lower()
            if file_extension not in allowed_extensions:
                messages.error(request, "Invalid file format. Only .doc, .docx files are allowed.")
                return redirect("home")

            try:
                try:
                    jobseeker_profile.objects.get(user_id=uid)
                except jobseeker_profile.DoesNotExist:
                    show_modal = True

                documents_dir = os.path.join(settings.MEDIA_ROOT, "documents")
                os.makedirs(documents_dir, exist_ok=True)

                fs = FileSystemStorage(location=documents_dir)
                saved_filename = fs.save(uploaded_file.name, uploaded_file)
                file_path = fs.path(saved_filename)

                # Enhanced extraction based on file type
                if file_extension in ('.doc', '.docx'):
                    document = Document(file_path)
                    paragraphs = [p.text for p in document.paragraphs if p.text.strip()]
                    content = "\n".join(paragraphs)

                # Remove the file after processing
                os.remove(file_path)

                # Extract resume details using the improved extraction function
                extracted_details = extract_resume_details(content)
                essential_fields = ["name", "email", "phone", "address", "skills", "university"]
                if any(not extracted_details.get(field) for field in essential_fields):
                    messages.error(request, "Failed to extract essential details from your resume. Check your file and try again.")
                    return redirect("home")

                # Save the resume file in the database after successful extraction
                jobseeker_resumeobj = jobseeker_resume(file=uploaded_file, user_id=uid)
                jobseeker_resumeobj.save()

            except Exception as e:
                messages.error(request, f"Error processing document: {str(e)}")
                return redirect("home")
    resume = jobseeker_resume.objects.filter(user_id=uid)
    job=job_title.objects.all()
    context = {
        "resume_details": extracted_details,
        "alert_message": alert_message,
        "fname": fname,
        "email": jobseek_email,
        "phone": phone,
        "show_modal": show_modal,
        "resume": resume,
        "job":job
    }

    if not jobseeker_profile.objects.filter(name=fname).exists() and not jobseeker_resume.objects.filter(user=uid).exists():
        redirect('home')
    return render(request, "jobseeker_home.html", context)


def jobseeker_profile_update(request):
    userid = request.session.get('jobseeker_id')
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
        percentage=request.POST.get('Percentage')
        passout=request.POST.get('passout')
        skills = request.POST.get('skills')
        image = request.FILES.get('image')
        job_preference = request.POST.get('job_preferences')
        # Fetch the first resume for the user (if multiple exist)
        resume = jobseeker_resume.objects.filter(user=userid).first()
        cv = resume.file if resume else None  # Handle case where no resume exists
        job_preference=job_title.objects.get(id=job_preference).job_title
        if jobseeker_profile.objects.filter(name=name).exists() and jobseeker_profile.objects.filter(email=email).exists():
            messages.error(request, "A Jobseeker with this name and/or email already exists. Please use different details.")
        else:
            jobseeker_obj = jobseeker_profile()
            jobseeker_obj.name = name
            jobseeker_obj.email = email
            jobseeker_obj.dob = dob
            jobseeker_obj.highest_qualification = qualification
            jobseeker_obj.percentage=percentage
            jobseeker_obj.passoutyear=passout
            jobseeker_obj.skills = skills
            jobseeker_obj.job_preference = job_preference
            jobseeker_obj.university = university
            jobseeker_obj.address = address
            jobseeker_obj.phone = phone
            jobseeker_obj.profile_img = image
            jobseeker_obj.user_id = userid
            jobseeker_obj.resume = cv
            jobseeker_obj.save()
            request.session['address'] = jobseeker_obj.address
            request.session['dob'] = jobseeker_obj.dob
            messages.success(request, "Updated profile successfully.Now you can use whole features of this portal.")
    return redirect('home')


def main(request):
    return render(request, 'index.html')


def base(request):
    jbid = request.session.get('jobseeker_id')
    if jobseeker_profile.objects.filter(user=jbid).exists():
        jsdt = jobseeker_profile.objects.get(user=jbid)
        return render(request, 'base.html', jsdt)
    else:
        jsdt = None
    return render(request, 'base.html', jsdt)


def Register(request):
    name = ""
    email = ""
    password = ""
    if request.method == "POST": 
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('Phone')
        if Jobseeker_Registration.objects.filter(name=name).exists() or Jobseeker_Registration.objects.filter(email=email).exists():
            messages.error(request, "A Jobseeker with this name and/or email already exists.You can Login directly.")
        else:
            jobseeker_obj = Jobseeker_Registration()
            jobseeker_obj.name = name
            jobseeker_obj.email = email
            jobseeker_obj.password = password
            jobseeker_obj.phone = phone
            jobseeker_obj.save()
            messages.success(request, "Jobseeker registered successfully!.Email will be your Username")
            return render(request, 'jobseeker_register.html')
    return render(request, 'jobseeker_register.html')


def reset_password(request, user_id):
    try:
        user = Jobseeker_Registration.objects.get(pk=user_id)
    except Jobseeker_Registration.DoesNotExist:
        messages.error(request, "Invalid password reset link.")
        return redirect("forgot_password")

    if request.method == "POST":
        new_password = request.POST.get("get_password")
        confirm_password = request.POST.get("confirm_password")

        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
        else:
            user.password = new_password  # This should be hashed (use Django's set_password)
           
            user.save()
            messages.success(request, "Your password has been reset successfully.")
            return redirect("jobseeker_login")  # Redirect after reset

    return render(request, "j_reset_password.html", {"user_id":user_id})


def Forgot_pwd(request):
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            user = Jobseeker_Registration.objects.get(email=email)
            uid = user.id
            # Send email without link
            reset_url = f"{settings.SITE_URL}/reset_password/{uid}/"
            
            # Send the email
            send_mail(
                subject="Password Reset Request",
                message=f"Click the link below to reset your password:\n{reset_url}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )
            messages.success(request, "Password reset instructions have been sent to your email.")
        except Jobseeker_Registration.DoesNotExist:
            messages.error(request, "Email not found. Please enter a registered email.")

    return render(request, "forgot-password.html")


def user_base(request):
    return render(request, 'base.html')


def jobseeker_logout(request):
    logout(request)
    request.session.clear()
    messages.success(request, "Logout Successfully")
    return render(request, 'jobseeker_login.html')


def company_logout(request):
    logout(request)
    request.session.clear()
    messages.success(request, "Logout Successfully")
    return render(request, 'company_login.html')


def search_job(request):
    # Get the jobseeker name from session and check if the profile exists
    fname = request.session.get('jobseeker_name')
    if not jobseeker_profile.objects.filter(name=fname).exists():
        return redirect('home')
    
    jobseeker = jobseeker_profile.objects.get(name=fname)
    jobs = company_joblist.objects.all()

    # Get search parameters from GET request
    search_query = request.GET.get('search', '')
    location_query = request.GET.get('location', '')
    
    # Filter by search query. For the foreign key job_title, traverse to its text field.
    if search_query:
        jobs = jobs.filter(
        Q(job_title__job_title__istartswith=search_query) | 
        Q(company__name__icontains=search_query) | 
        Q(job_type__icontains=search_query)
        )
    
    # Filter by location query
    if location_query:
        jobs = jobs.filter(location__icontains=location_query)
    
    context = {
        "fname": fname,
        "jobs": jobs,
        "jsdt": jobseeker,
    }
    return render(request, 'search-job.html', context)


def coverletter(request):
    job = job_title.objects.all()
    company = Company.objects.all()
    fname = request.session.get('jobseeker_name')
    email = request.session.get('jobseeker_email')
    phoneno = request.session.get('jobseeker_phone')
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
        address = request.POST.get("Address")
        eligibility = request.POST.get('eligibility')
        ldate = date.today().strftime('%d-%m-%Y')
        try:
            company_obj = Company.objects.get(id=company_id)
            company_name = company_obj.name
            company_loc = company_obj.address
            job_position = job_title.objects.get(id=position)
            jobs = job_position.job_title
            job_id=jobs
        except Company.DoesNotExist:
            company_name = "Unknown Company"

        # OpenAI API Call for Cover Letter Generation
        prompt = f"""
Write a professional and engaging cover letter for a fresher job seeker named {name} , whose address is {address} ,email is {email},having qualification of '{eligibility}' and phone number is {phone}. 
The job seeker is applying for a {job_type} position as {jobs} at {company_name}, located at {company_loc}. 

Address the letter to {hr_name}, incorporating the company's full address. Highlight relevant skills such as {skills} and ensure the letter is formatted in a common professional style without placeholders like [Your Name] or [Your Address]. 

Include the date ({ldate}) at the beginning and conclude with a proper closing, using the candidate’s full name instead of placeholders. Keep the letter concise, engaging, and directly relevant to the job opportunity.
"""
        
        response = openai.ChatCompletion.create(# pylint: disable=undefined-variable

             model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": prompt}
  ]
        )
        request.session['company_id']=company_id
        request.session['highest_qualification']=eligibility
        cover_letter = response["choices"][0]["message"]["content"].strip()
        jsdt = jobseeker_profile.objects.get(email=email)
        return render(request, "cover-letter.html", {
            "fname": fname,
            "email": email,
            "cover_letter": cover_letter,
            "company": company,
            "phone":phoneno,
            "jsdt":jsdt,
            "job":job,
            "job_id":job_id
        })
    jsdt = jobseeker_profile.objects.get(email=email)
    return render(request, "cover-letter.html", {
        "fname": fname,
        "company": company,
        "email": email,
        "phone":phoneno,
        "job":job,
        "jsdt":jsdt
    })

def send_cover_letter_email(request):
    fname=request.session.get('jobseeker_name')
    highest_qualification=request.session.get('highest_qualification')
    
    if request.method == "POST":
        cid = request.session.get("company_id")
        pdf_file = request.FILES.get("pdf")
        job_title_id=request.POST.get('job_id')
        email=Company.objects.get(id=cid).email
        if not cid or not pdf_file:
            return JsonResponse({"message": "Missing email or PDF!"}, status=400)
        job=job_title.objects.get(id=job_title_id).job_title
        # Save the uploaded PDF to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
            for chunk in pdf_file.chunks():
                temp_pdf.write(chunk)

            temp_pdf_path = temp_pdf.name

        # Send email
        email_message = EmailMessage(
            subject=f"{ fname }'s Job Application for { job }",
            body=f" Dear Hiring Manager,\n\n I hope this email finds you well. I am writing to express my interest in the { job } position at your company. With my qualification in { highest_qualification }, I am eager to contribute my skills and expertise to your esteemed organization.\n\nI have attached my cover letter for your review.\n\n It highlights my skills and explains how my experience aligns with the requirements of the role. I would greatly appreciate the opportunity to discuss how I can be a valuable addition to your team.Please feel free to reach out if you require any further information. I look forward to the possibility of an interview at your convenience.\n\nThank you for your time and consideration.\n\nBest regards, \n\n{fname}",
            from_email=settings.DEFAULT_FROM_EMAIL,  
            to=[email],
        )
        email_message.attach_file(temp_pdf_path)
        email_message.send()
        return JsonResponse({"message": "Cover Letter sent successfully!"})
    return JsonResponse({"message": "Invalid request method"}, status=400)
def settings_view(request): 
    jbid = request.session.get('jobseeker_id')
    try: 
        jsdt = jobseeker_profile.objects.get(user_id=jbid)
        fname = request.session.get('jobseeker_name')
        jobseek_email = request.session.get('jobseeker_email') 
        phone = request.session.get('jobseeker_phone')
        # address=request.session.get("address")
        context = {
            'jsdt':jsdt,
                "fname":fname,
                "email":jobseek_email,
                "phone":phone,
            }
        return render(request, 'settings_view.html', context)
    except:
        
        jsdt = Jobseeker_Registration.objects.filter(id=jbid)
        fname = request.session.get('jobseeker_name')
        if not jobseeker_profile.objects.filter(name=fname).exists():
            return redirect('home')
        context = {
            'jsdt':jsdt,
                "fname":fname,
              
            }
        return render(request, 'settings_view.html', context)


def support(request):
    fname = request.session.get('jobseeker_name')
    if not jobseeker_profile.objects.filter(name=fname).exists():
            return redirect('home')
    jobseeker = jobseeker_profile.objects.get(name=fname)
    return render(request, 'support.html', {"fname":fname, "jsdt":jobseeker})


def mockinterview(request):
    fname = request.session.get('jobseeker_name')
    if not jobseeker_profile.objects.filter(name=fname).exists():
            return redirect('home')
    jobs = job_title.objects.all()
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
            response = openai.ChatCompletion.create(# pylint: disable=undefined-variable

                model="gpt-4o-mini",
                messages=[{"role": "system", "content": prompt}]
            )

            content = response["choices"][0]["message"]["content"].strip()
            # Split questions by newline and filter out empty strings
            questions = [q for q in content.split("\n") if q.strip()]
            # Ensure that exactly 5 questions are returned
            if len(questions) != 5:
                return JsonResponse({"error": "Failed to generate exactly 5 interview questions. Please try again."}, status=400)
            return JsonResponse({"questions": questions})

        else:
            # Evaluate the user answer
            prompt = f"Evaluate this job interview response for a {job.job_title} role and provide constructive feedback. Do not include any introduction or pleasantries. Answer concisely.\n\nAnswer: {user_answer}"
            response = openai.ChatCompletion.create(# pylint: disable=undefined-variable
                model="gpt-4o-mini",
                messages=[{"role": "system", "content": prompt}]
            )
            feedback = response["choices"][0]["message"]["content"].strip()
            return JsonResponse({"feedback": feedback})
    jobseeker = jobseeker_profile.objects.get(name=fname)
    return render(request, 'mock-interview.html', {'job': jobs, "fname":fname, "jsdt":jobseeker})

def parse_list(text):
    """
    Parse a comma-separated string into a set of lowercase trimmed items.
    """
    if text:
        return set([item.strip().lower() for item in text.split(",") if item.strip()])
    return set()

def match_jobs(jobseeker):
    """
    Match jobs based on overlapping skills and jobseeker's highest qualification.
    Returns a QuerySet of matching company_joblist jobs.
    """
    # Function to extract numeric percentage value from string
    def extract_percentage(value):
        try:
            return float(value.strip('%')) if value else 0.0
        except ValueError:
            return 0.0
    # Parse jobseeker skills and qualification
    seeker_skills = parse_list(jobseeker.skills)
    seeker_qual = jobseeker.highest_qualification.strip().lower() if jobseeker.highest_qualification else ""
    seeker_percentage = extract_percentage(jobseeker.percentage) if jobseeker.percentage else 0.0
    # Fetch all jobs (this could be optimized with a filter, but for now we'll do it in Python)
    all_jobs = company_joblist.objects.all()
    matching_jobs = []
    for job in all_jobs:
        job_skills = parse_list(job.skills_required)
        job_percentage_criteria = extract_percentage(job.percent_criteria)
        
        # Check for any common skills
        if not seeker_skills.intersection(job_skills):
            continue
        
        # Check eligibility: if job.highest_qualification exists, see if it matches the seeker qualification
        if job.highest_qualification:
            # Split eligibility criteria if multiple (assuming comma-separated)
            eligibility_set = parse_list(job.highest_qualification)
            if seeker_qual and seeker_qual not in eligibility_set:
                continue
            # Check if jobseeker's percentage meets or exceeds the job's percentage criteria
        if seeker_percentage < job_percentage_criteria:
            continue
        matching_jobs.append(job)
    return matching_jobs

def auto_apply_jobs(jobseeker, max_apply=4):
    """
    Auto-apply function:
    - Shortlists matching jobs (using skills and eligibility).
    - Excludes jobs that the jobseeker has already applied for.
    - Limits to max_apply new applications.
    """
    # Get list of job IDs that the jobseeker has already applied for
    applied_job_ids = JobApplication.objects.filter(jobseeker=jobseeker).values_list('company_joblist_id', flat=True)

    # Get matching jobs based on skills and eligibility
    matching_jobs = match_jobs(jobseeker)

    # Exclude jobs already applied for
    available_jobs = [job for job in matching_jobs if job.id not in applied_job_ids]

    # Sort by dateofpublish (newest first), handling None values
    available_jobs.sort(key=lambda x: x.dateofpublish or "", reverse=True)

    applications_made = 0
    for job in available_jobs[:max_apply]:
        try:
            JobApplication.objects.create(jobseeker=jobseeker, company_joblist=job)
            applications_made += 1
        except Exception as e:
            print(f"Error applying for {job.job_title}: {e}")
            continue

    return applications_made, available_jobs

def autoapply(request):
    # Use session to retrieve jobseeker email instead of just name
    fname=request.session.get('jobseeker_name')
    jobseeker_email = request.session.get('jobseeker_email')
    if not jobseeker_email or not jobseeker_profile.objects.filter(email=jobseeker_email).exists():
        messages.error(request, "Jobseeker profile not found.")
        return redirect('home')

    jobseeker = jobseeker_profile.objects.get(email=jobseeker_email)
    recommended_jobs = match_jobs(jobseeker)
    recommended_jobs=sorted(recommended_jobs, key=lambda x: x.Lastdate)
    # On POST request, perform auto-apply action
    if request.method == "POST":
        applications, _ = auto_apply_jobs(jobseeker, max_apply=4)
        if applications:
            messages.success(request, f"Auto-applied to {applications} job(s) successfully!")
        else:
            messages.info(request, "No new matching jobs available for auto-apply.")
        redirect('auto-apply')

    context = {
        "jobseeker_email": jobseeker_email,
        "jsdt": jobseeker,
        "fname":fname,
        "recommended_jobs": recommended_jobs,
    }
    return render(request, "auto-apply.html", context)

def applied_jobs(request):
    fname = request.session.get('jobseeker_name')
    if not fname or not jobseeker_profile.objects.filter(name=fname).exists():
        return redirect('home')
    profile=jobseeker_profile.objects.get(name=fname)
    profile_id=profile.id
    jobseeker = jobseeker_profile.objects.get(name=fname)
    jobs=JobApplication.objects.filter(jobseeker_id=profile_id)
    jobs=sorted(jobs, key=lambda x: x.id)
    context = {
        "fname": fname,
        "jsdt": jobseeker,
        "jobs":jobs
        # "recommended_jobs": recommended_jobs,
    }
    return render(request,'applied-jobs.html',context)

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
        comp_logo = request.FILES.get('company_logo')
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
            companyobj.profile_img = comp_logo
            companyobj.save()
            messages.success(request, "Company registered successfully!.Email will be your Username")
            return redirect('company_registration')
    company = Company_Type_Master.objects.all()
    context = {
        'company':company
    }
    return render(request, 'company_registration.html', context)

def change_password(request):
    fname = request.session.get('jobseeker_name')
    
    if not fname or not jobseeker_profile.objects.filter(name=fname).exists():
        return redirect('home')
    
    jobseeker = jobseeker_profile.objects.get(name=fname)
    user=Jobseeker_Registration.objects.get(name=fname)
    exist_pwd=user.password
    if request.method == "POST":
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('get_password')
        confirm_password = request.POST.get('confirm_password')
        
        if exist_pwd != old_password:
            messages.error(request, "Old password is incorrect.")
        elif new_password != confirm_password:
            messages.error(request, "New passwords do not match.")
        elif len(new_password) < 4:
            messages.error(request, "Password must be at least 4 characters long.")
        else:
            userobj=Jobseeker_Registration.objects.get(name=fname)
            userobj.password=confirm_password
            userobj.save()
            messages.success(request, "Your password has been updated successfully!")

    context = {"fname": fname, "jsdt": jobseeker}
    return render(request, 'change_pwd.html', context)


def company_change_password(request):
    cname = request.session.get('company_name')
    cid = request.session.get('company_id')
    comp = Company.objects.get(id=cid)
    exist_pwd=comp.password
    if request.method == "POST":
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('get_password')
        confirm_password = request.POST.get('confirm_password')
        
        if exist_pwd != old_password:
            messages.error(request, "Old password is incorrect.")
        elif new_password != confirm_password:
            messages.error(request, "New passwords do not match.")
        elif len(new_password) < 4:
            messages.error(request, "Password must be at least 4 characters long.")
        else:
            compobj=Company.objects.get(name=cname)
            compobj.password=confirm_password
            compobj.save()
            messages.success(request, "Your password has been updated successfully!")

    context = {
            # "jobs": expiredyet,
            "cname": cname,
            "compdt":comp,
    }
    return render(request, 'company_change_pwd.html', context)

def delete_user_profile(request):
    fname = request.session.get('jobseeker_name')
    
    if not fname or not jobseeker_profile.objects.filter(name=fname).exists():
        return redirect('home')
    if(JobApplication.objects.filter(jobseeker__name=fname).exists()):
        JobApplication.objects.filter(jobseeker__name=fname).delete()
        
    jobseeker = jobseeker_profile.objects.get(name=fname)
    jobseeker.delete()
    jobseeker_resume.objects.get(user__name=fname).delete()
    return redirect('settings_view')
    

def delete_job(request): 
    cname = request.session.get('company_name')
    job_id = request.GET.get("ids")
    messages.success(request, f"jobid:{str(job_id)}")
    if not job_id:
            messages.error(request, "Job ID is missing in request.")
            return render(request, 'company_jobs.html', {'cname': cname})
        
    try:
            if(JobApplication.objects.filter(company_joblist__company__name=cname,company_joblist__id=job_id).exists()):
                applications=get_object_or_404(JobApplication,company_joblist__company__name=cname,company_joblist__id=job_id)
                applications.delete()
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


def jobs(request):
    if request.method == "POST":
        job_title1 = request.POST.get('job')
        company_typeobj = job_title()
        company_typeobj.job_title = job_title1
        company_typeobj.save()
        messages.success(request, "Job title added successfully!")
        return render(request, 'job_position.html')
    return render(request, 'job_position.html')


def company_reset_pwd(request, comp_id):
    try:
        comp = Company.objects.get(pk=comp_id)
    except Company.DoesNotExist:
        messages.error(request, "Invalid password reset link.")
        return redirect("forgot_password")

    if request.method == "POST":
        new_password = request.POST.get("get_password")
        confirm_password = request.POST.get("confirm_password")

        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
        else:
            comp.password = new_password  # This should be hashed (use Django's set_password)
            comp.save()
            messages.success(request, "Your password has been reset successfully.")
            return redirect("company_login")  # Redirect after reset

    return render(request, "company_reset_password.html", {"comp_id":comp_id})


def company_forgot_password(request):
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            cmpny = Company.objects.get(email=email)
            uid = cmpny.id
            # Send email without link
            reset_url = f"{settings.SITE_URL}/company_reset_password/{uid}/"
            
            # Send the email
            send_mail(
                subject="Password Reset Request",
                message=f"Click the link below to reset your password:\n{reset_url}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )
            
            messages.success(request, "Password reset instructions have been sent to your email.")
        except Company.DoesNotExist:
            messages.error(request, "Email not found. Please enter a registered email.")
    return render(request, 'company_forgot_pwd.html')


def company_dashboard(request):
    try:
        cname = request.session.get('company_name')
        cid = request.session.get('company_id')
        comp = Company.objects.get(id=cid)
        # Fetch all job listings for the logged-in company
        compjobdt = company_joblist.objects.filter(company_id=cid)
        participants=JobApplication.objects.filter(company_joblist__company_id=cid)
        latest_applications=participants.order_by('-id')[:3]
        pcount=participants.count()
        # If no jobs exist, show the default page
        if not compjobdt.exists():
            count = 0
            return render(request, 'company_dashboard.html', {"cname": cname, "count":count, "compdt":comp,"pcount":pcount,"participants":latest_applications}) # type: ignore
        
        # Get expired jobs
       
        count = compjobdt.count()  # Count jobs for the logged-in company
        context = {
            # "jobs": expiredyet,
            "cname": cname,
            "count":count,
            "compdt":comp,
            "pcount":pcount,
            "participants":latest_applications
        }
        return render(request, 'company_dashboard.html', context)
    except Exception as e:
        # Handle unexpected errors
        return render(request, 'company_dashboard.html', {"cname": cname, "compdt":comp, "error": str(e)})

    
def company_settings(request):
    cid = request.session.get('company_id')
    compdt = Company.objects.get(id=cid)
    cmail = compdt.email
    cname = compdt.name
    cloc = compdt.address
    ctype = compdt.company_type.company_type
    company = Company.objects.get(id=cid)
    context = {
            "cname":cname, "cmail":cmail, "cloc":cloc,
            "ctype":ctype, "cid":cid, "compdt":company
        } 
    if request.method == "POST":
        comp_logo = request.FILES.get('company_logo')
        comp = Company.objects.get(id=cid)
        if comp_logo: 
            comp.profile_img = comp_logo
            comp.save()
            messages.success(request, "Logo Uploaded successfully!!")    
        return render(request, 'company_settings_view.html', context)
    return render(request, 'company_settings_view.html', context)


def company_jobs(request):
    try:
        cname = request.session.get('company_name')
        cid = request.session.get('company_id')
        company = Company.objects.get(id=cid)
        # Fetch all job listings for the logged-in company
        compjobdt = company_joblist.objects.filter(company=cid)
        # If no jobs exist, show the default page
        if not compjobdt.exists():
            return render(request, 'company_jobs.html', {"cname": cname, "compdt":company})
        
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
            "compdt":company
        }
        return render(request, 'company_jobs.html', context)
    
    except Exception as e:
        # Handle unexpected errors
        return render(request, 'company_jobs.html', {"cname": cname, 'compdt':company, "error": str(e)})


def company_postjob(request):
    job = job_title.objects.all()
    cid = request.session.get('company_id')
    company = Company.objects.get(id=cid)
    if request.method == "POST":
        job_number = request.POST.get('job_number')
        job_position = request.POST.get('job_title')
        job_description = request.POST.get('job_description')
        job_location = request.POST.get('Location')
        job_type = request.POST.get('Job_type')
        jobposted_date = request.POST.get('jobposted_date')
        qualification = request.POST.getlist('highest_qualification')
        percent_criteria=request.POST.get('percentage')
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
            companyjob_obj.percent_criteria=percent_criteria
            companyjob_obj.skills_required = skills_str
            companyjob_obj.Lastdate = lastdate
            companyjob_obj.save()
            messages.success(request, "Job Posted Successfully!!")        
    cname = request.session.get('company_name')
    return render(request, 'company_postjob.html', {"cname":cname, "compdt":company, 'cdate':date.today().strftime("%Y-%m-%d"), "job":job})


def edit_job(request):
    job = job_title.objects.all()
    cid = request.session.get('company_id')
    cname = request.session.get('company_name')
    company = Company.objects.get(id=cid)
    if request.method == "POST":
        job_id = request.POST.get('job_id')
        job_number = request.POST.get('job_number')
        job_position = request.POST.get('job_title')
        job_description = request.POST.get('job_description')
        job_location = request.POST.get('location')
        job_type = request.POST.get('job_type')
        # jobposted_date = request.POST.get('jobposted_date')
        qualification = request.POST.getlist('highest_qualification')
        percent_criteria=request.POST.get('percentage')
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
        companyjob_obj.percent_criteria=percent_criteria
        companyjob_obj.skills_required = skills_str
        companyjob_obj.Lastdate = lastdate
        companyjob_obj.save()
        messages.success(request, "Job Edited Successfully!!") 
        return redirect('job_listing')
    jobid = request.GET.get('ids')
    jobobg = company_joblist.objects.get(id=jobid)
    context = {
        'jobobg':jobobg,
        "cname":cname,
        "job":job,
        "compdt":company
    }
    return render(request, 'edit-job.html', context)

def applications(request):
    cid = request.session.get('company_id')
    cname = request.session.get('company_name')
    company = Company.objects.get(id=cid)
    Applicants=JobApplication.objects.filter(company_joblist__company_id=cid)
    # Sort the list of applicants by job title
    Applicants = sorted(Applicants, key=lambda x: x.company_joblist.job_title.job_title)
    # Group applicants by job title
    grouped_applicants = {}
    for job_title, group in groupby(Applicants, key=lambda x: x.company_joblist.job_title.job_title):
            grouped_applicants[job_title] = list(group)
    context = {
        "cname":cname,
        "compdt":company,
        "Applicants":Applicants,
        "grouped_applicants":grouped_applicants
    }
    return render(request,'applications.html',context)
def jobseeker_dashboard(request):
    fname = request.session.get('jobseeker_name')
    if not jobseeker_profile.objects.filter(name=fname).exists():
        return redirect('home')
    ccount = company_joblist.objects.all()
    profile=jobseeker_profile.objects.get(name=fname)
    profile_id=profile.id
    applied_jcount=JobApplication.objects.filter(jobseeker_id=profile_id)
    ajcount=applied_jcount.count()
    company = Company.objects.all()
    jcount = ccount.count()
    compcount = company.count()
    jobseeker = jobseeker_profile.objects.get(name=fname)
    return render(request, 'jobseeker_dashboard.html', {"fname":fname, "jcount":jcount, "compcount":compcount, "company":company, "jsdt":jobseeker,"ajcount":ajcount})

