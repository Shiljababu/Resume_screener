from django.contrib import admin
from .models import Job_Description, Resume, MatchScore
# Register your models here.

admin.site.register(Job_Description)
admin.site.register(Resume)
admin.site.register(MatchScore)