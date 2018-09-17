from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect

from main_app.forms import *
from main_app.util import *

import string
from random import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def committee(request):
    return render(request, 'committee.html')

def core_course(request):
    return render(request, 'core_course.html')

def faculty(request):
    return render(request, 'faculty.html')

def internship_postings(request):
    return render(request, 'internship_postings.html')

def partners(request):
    return render(request, 'partners.html')

def principles_foundations(request):
    return render(request, 'principles_foundations.html')

def program(request):
    return render(request, 'program.html')

def technology_enablers(request):
    return render(request, 'technology_enablers.html')

def under_construction(request):
    return render(request, 'under_construction.html')

########## INTERNSHIP PORTAL STUFF

def signin(request):

    return_dict = {'signInForm': SignInForm, 'createAccountForm': CreateAccountForm}

    if request.method == "GET":
        return render(request, 'registration/login.html', return_dict)
    else:
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print("username: %s, password: %s" %(username,password))
            user = authenticate(username=username, password=password)
            if user is not None:
                return HttpResponseRedirect("/")
            else:
                return_dict['errors'] = "Don't match. Try again!"
                return render(request, 'registration/login.html', return_dict)

        else:
            return_dict['errors'] = "Invalid input. Try again!"
            return render(request, 'registration/login.html', return_dict)

def signup(request):

    return_dict = {'signInForm': SignInForm, 'createAccountForm': CreateAccountForm}

    if request.method == "GET":
        return render(request, 'registration/login.html', return_dict)

    if request.method == 'POST':

        form = CreateAccountForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')

            username = first_name+"."+last_name

            # generate password
            characters = string.ascii_letters + string.punctuation  + string.digits
            password =  "".join(choice(characters) for x in range(randint(8, 16)))

            # create user
            try:
                user = User.objects.create_user(username, email, password)
                user.first_name = first_name
                user.last_name = last_name

                print("first_name: %s, last_name: %s, email: %s, username: %s, password: %s" %(first_name, last_name, email, username,password))

                user.save()
            except Exception as e:
                return_dict['errors'] = "Invalid input. Try again!"
                return render(request, 'registration/login.html', return_dict)

            else:
                # Not really error, work on aesthetics (like diff. msgs with diff. dialogs later)
                return_dict['errors'] = "Successfully created user!"
                send_user_account_email(email,first_name, username,password)
                return render(request, 'registration/login.html', return_dict)
