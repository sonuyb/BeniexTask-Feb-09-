from django.urls import path, include
from . import views

urlpatterns = [
    path('regseeker/', views.registerjobseeker, name='regseeker'),
    path('',views.seekerdash,name='seekerdash'),
    path('profile/', views.jobseekerprofile, name='profile'),
    # path('update/', views.jobseekerprofileupdate, name='update'),
    path('job-listing/', views.display_all_job, name='applicant_job_listing'),
    path('job-apply/<pk>', views.apply_job, name='job-apply'),
    path('edit-profile/<pk>',views.editprofile,name='editprofile'),
    path('applied-job',views.applied_jobs,name='applied_job'),
    path('seeker_logout',views.seeker_logout,name='seekerlogout')
]
