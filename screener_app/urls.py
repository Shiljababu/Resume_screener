from django.urls import path

from screener_app.views import home, logout_view, upload_job_description, upload_resume, view_results


urlpatterns = [
    path('', home, name='home'),
    path('upload-resume/', upload_resume, name='upload_resume'),
    path('upload-jd/', upload_job_description, name='upload_jd'),
    path('results/', view_results, name='view_results'),  
    path('logout/', logout_view, name='logout'),
]


