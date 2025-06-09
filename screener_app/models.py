from django.db import models

# Create your models here.

class Job_Description(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
    
class Resume(models.Model):
    name = models.CharField(max_length=100)
    resume_file = models.FileField(upload_to = 'resumes/')
    uploaded_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
    
class MatchScore(models.Model):
    job_description = models.ForeignKey(Job_Description, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return f"{self.resume.name} ↔ {self.job_description.title} = {self.score}"
