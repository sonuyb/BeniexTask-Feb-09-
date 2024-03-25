from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # is_applicant = models.BooleanField(default=False)
    # is_employer = models.BooleanField(default=False)
    USER_TYPE_CHOICES = [
        ('JOB_SEEKER', 'JOB_SEEKER'),
        ('EMPLOYER', 'EMPLOYER'),
    ]
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
