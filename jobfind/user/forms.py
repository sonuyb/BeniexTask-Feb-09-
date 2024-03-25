from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200)
    # is_applicant = forms.BooleanField(label='Are you an Job Seeker?', required=False)
    # is_employer = forms.BooleanField(label='Are you an Employer?', required=False)
    # user_type = forms.ChoiceField(choices=[(True, 'is_applicant'), (False, 'is_employer')], label='User Type')
    # USER_TYPE_CHOICES = (
    #     ('applicant', 'Applicant'),
    #     ('employer', 'Employer'),
    # )
    user_type = forms.ChoiceField(choices= CustomUser.USER_TYPE_CHOICES, label='Select User Type')
    # user_type = forms.ChoiceField(choices= UserTypeChoices, label='Select User Type')


    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'user_type')

        error_messages = { }