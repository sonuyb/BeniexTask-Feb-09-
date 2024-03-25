from django.db import models
from user.models import *
from jobseeker.models import *

class Job(models.Model):
    job_title = models.CharField(max_length=100)
    salary = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,  related_name='jobs')
    job_requirement = models.TextField()
    is_available = models.BooleanField()

class JobApplicant(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)