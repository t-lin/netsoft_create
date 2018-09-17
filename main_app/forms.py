#from snowpenguin.django.recaptcha2.fields import ReCaptchaField
#from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget
from django import forms


class SignInForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

class CreateAccountForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
