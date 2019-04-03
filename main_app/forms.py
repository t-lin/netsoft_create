from django import forms
from main_app.choices import *

class SignInForm(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

class ChangePassForm(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput())
    new_password = forms.CharField(widget=forms.PasswordInput())

class CreateAccountForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)

class UploadResumeForm(forms.Form):
    resume = forms.FileField(
        label = 'Select a file',
        help_text = 'Max. 10 MB'
    )

class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    university = forms.ChoiceField(
        choices=UNIVERSITY_CHOICES,
        widget=forms.Select(),
        required=True)
    degree = forms.ChoiceField(
        choices=DEGREE_CHOICES,
        widget=forms.RadioSelect,
        required=True)
    courses = forms.MultipleChoiceField(
        choices=COURSES_CHOICES,
        widget=forms.CheckboxSelectMultiple(),
        required=False)
