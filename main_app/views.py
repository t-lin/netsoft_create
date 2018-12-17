from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from netsoft_create import settings
from main_app.forms import *
from main_app.models import *
from django.contrib import messages

import main_app.util as util
import os

########## STATIC PAGES ##########

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


########## INTERNSHIP PORTAL STUFF ##########

@login_required
def internship_profile(request):

    resumes = Resume.objects.filter(username = request.user.username)

    print(resumes.values())
    profile = Profile.objects.filter(username = request.user.username).values()
    print(profile)

    return_dict = {'UploadResumeForm': UploadResumeForm, 'resumes': resumes, 'ProfileForm': ProfileForm, 'profile': profile}
    return render(request,'internship/profile.html', return_dict)

@login_required
@require_http_methods(["POST"])
def save_profile(request):

    for key in request.POST:
        print("%s: %s" %(key, request.POST[key]))

    form = ProfileForm(request.POST or None)
    if form.is_valid():

        tech_enablers = False
        princ_foundations = False

        if "technologies_enablers" in request.POST.getlist("courses"):
            tech_enablers = True

        if "principles_foundations" in request.POST.getlist("courses"):
            princ_foundations = True

        profile = Profile.objects.filter(username = request.user.username)
        if profile:

            Profile.objects.filter(username = request.user.username).update(
                first_name = form.cleaned_data.get("first_name"),
                last_name = form.cleaned_data.get("last_name"),
                university = form.cleaned_data.get("university"),
                degree = form.cleaned_data.get("degree"),
                technology_enablers = tech_enablers,
                principles_foundations = princ_foundations
            )
        else:

            new_profile = Profile(username = request.user.username,
                first_name = form.cleaned_data.get("first_name"),
                last_name = form.cleaned_data.get("last_name"),
                university = form.cleaned_data.get("university"),
                degree = form.cleaned_data.get("degree"),
                technology_enablers = tech_enablers,
                principles_foundations = princ_foundations
            )

            new_profile.save()
        return HttpResponseRedirect("/internship/profile/")
    else:
        curr_profile = Profile.objects.filter(username = request.user.username).values()
        return render(request, 'internship/profile.html', {'ProfileForm': form, 'profile': curr_profile})


@login_required
@require_http_methods(["POST"])
def upload_resume(request):

    form = UploadResumeForm(request.POST, request.FILES)
    if form.is_valid():
        newresume = Resume(resume = request.FILES['resume'], username = request.user.username)
        newresume.save()

        return HttpResponseRedirect("/internship/profile/")
    else:
        return render(request, 'internship/profile.html', {'form': form})


@login_required
@require_http_methods(["POST"])
def delete_resume(request):

    resume = request.POST['resume']

    # remove the requested resumes to be deleted
    resumes = Resume.objects.filter(resume = resume, username = request.user.username).delete()

    file_location = settings.MEDIA_ROOT+'/'+resume
    print(file_location)
    if os.path.exists(file_location):
      os.remove(file_location)

    return HttpResponseRedirect("/internship/profile/")


def signin(request):

    return_dict = {'signInForm': SignInForm, 'createAccountForm': CreateAccountForm}

    if request.user.is_authenticated:
        return HttpResponseRedirect("/internship/profile/")


    if request.method == "GET":
        return render(request, 'login.html', return_dict)
    else:
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return HttpResponseRedirect("/internship/profile/")
            else:
                return_dict['errors'] = "Your Username and/or Password does not match! Please try again."
        else:
            return_dict['errors'] = "Invalid input. Try again!"

        return render(request, 'login.html', return_dict)

def signout(request):
    logout(request)
    return HttpResponseRedirect("/signin/")


def signup(request):

    return_dict = {'signInForm': SignInForm, 'createAccountForm': CreateAccountForm}

    if request.method == "GET":
        return render(request, 'login.html', return_dict)

    if request.method == 'POST':

        form = CreateAccountForm(request.POST)
        if form.is_valid():

            recaptcha_response = request.POST.get('g-recaptcha-response')
            remote_ip = request.META['REMOTE_ADDR']

            result = util.verify_recaptcha(recaptcha_response, remote_ip)

            # verify RECAPTCHAv2
            if result["success"]:
                return_dict["errors"] = util.create_user(form)
            else:
                return_dict["errors"] = "RECAPTCHAv2 Failed. Please don't be a Bot ... Zuckerberg"
        else:
            return_dict['errors'] = "Invalid input. Try again!"

        return render(request, 'login.html', return_dict)
