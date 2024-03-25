from django.db import models
from user.models import CustomUser

class JobSeeker(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    highest_qualification = models.CharField(max_length=100)
    current_location = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resume/')
    cover_letter = models.FileField(upload_to='coverletter/')

