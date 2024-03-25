from django.urls import path
from . import views

urlpatterns = [
    path('',views.employeedash,name='regemp'),
    path('create-job',views.createjob,name='createjob'),
    path('job-listing/',views.display_job,name='job_listing'),
    path('edit/<pk>',views.edit,name='edit'),
    path('delete/<pk>',views.delete,name='delete'),
    path('view-applicants/<int:job_id>',views.view_applicants,name='view_applicants'),
    path('emp_logout',views.emp_logout,name='emplogout')
]
