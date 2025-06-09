from django.shortcuts import render, redirect
from .models import Resume, Job_Description, MatchScore
from .forms import Job_descriptionForm
from docx import Document
import pdfplumber
import os
from .utils import extract_text_from_pdf, extract_text_from_docx

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())

def extract_text_from_docx(file):
    doc = Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def home(request):
    return render(request, 'screener_app/home.html')

def upload_job_description(request):
    if request.method == 'POST':
        form = Job_descriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('upload_resume')
    else:
        form = Job_descriptionForm()
    return render(request, 'screener_app/upload_jd.html', {'form': form})

# def upload_resume(request):
#     job_descriptions = Job_Description.objects.all()

#     if request.method == 'POST':
#         name = request.POST.get('name')
#         jd_id = request.POST.get('job_description_id')
#         selected_jd = Job_Description.objects.get(id=jd_id)

#         for file in request.FILES.getlist('resume_files'):
#             resume_obj = Resume.objects.create(name=name, resume_file=file)
#             ext = os.path.splitext(file.name)[1]
#             if ext == '.pdf':
#                 resume_text = extract_text_from_pdf(file)
#             elif ext == '.docx':
#                 resume_text = extract_text_from_docx(file)
#             else:
#                 resume_text = "Unsupported format"

#             score = 0.0  # placeholder

#             MatchScore.objects.create(
#                 job_description=selected_jd,
#                 resume=resume_obj,
#                 score=score
#             )

#         return redirect('view_results')

#     return render(request, 'screener_app/upload_resume.html', {
#         'job_descriptions': job_descriptions
#     })

import os
from django.shortcuts import render, redirect, get_object_or_404

def upload_resume(request):
    job_descriptions = Job_Description.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        jd_id = request.POST.get('job_description_id')

        # Get the selected Job Description or 404 if not found
        selected_jd = get_object_or_404(Job_Description, id=jd_id)

        # Get all uploaded resume files
        files = request.FILES.getlist('resume_files')
        if not files:
            # Optionally handle case where no files uploaded
            return render(request, 'screener_app/upload_resume.html', {
                'job_descriptions': job_descriptions,
                'error': 'Please upload at least one resume file.'
            })

        for file in files:
            resume_obj = Resume.objects.create(name=name, resume_file=file)
            ext = os.path.splitext(file.name)[1].lower()

            # Extract text based on file type
            if ext == '.pdf':
                resume_text = extract_text_from_pdf(file)
            elif ext == '.docx':
                resume_text = extract_text_from_docx(file)
            else:
                resume_text = None  # Unsupported format
                # Optionally skip this file or notify user

            # TODO: Add your actual scoring logic here based on resume_text and selected_jd
            score = 0.0  # Placeholder for score calculation

            MatchScore.objects.create(
                job_description=selected_jd,
                resume=resume_obj,
                score=score
            )

        return redirect('view_results')

    return render(request, 'screener_app/upload_resume.html', {
        'job_descriptions': job_descriptions
    })


def view_results(request):
    results = MatchScore.objects.select_related('resume', 'job_description')
    return render(request, 'screener_app/result.html', {'results': results})


from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('home')  # or wherever you want to redirect after logout
