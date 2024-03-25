from django import forms
from . models import *

class JobSeekerRegister(forms.ModelForm):

    class Meta:
        model = JobSeeker
        fields = ['first_name','last_name','highest_qualification','current_location','resume','cover_letter']