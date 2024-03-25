from django.contrib import admin
from . models import *
from jobseeker.models import JobSeeker
from employer.models import Job,JobApplicant

admin.site.register(CustomUser)
admin.site.register(JobSeeker)
admin.site.register(Job)
admin.site.register(JobApplicant)