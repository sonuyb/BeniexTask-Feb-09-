from django import forms
from . models import *

class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ['id','job_title','salary','city','state','job_type','job_requirement','is_available']