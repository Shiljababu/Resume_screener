from django import forms
from .models import Resume, Job_Description

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'resume_file']


class Job_descriptionForm(forms.ModelForm):
    class Meta:
        model = Job_Description
        fields = '__all__'