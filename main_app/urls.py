#from django.contrib.auth.views import LoginView

from django.urls import path, re_path
import main_app.views as views

urlpatterns = [
    path('', views.index, name="index"),
    path('committee/', views.committee, name="committee"),
    path('core-courses/', views.core_course, name="core-courses"),
    path('faculty/', views.faculty, name="faculty"),
    path('internship-postings/', views.internship_postings, name="internship-postings"),
    path('partners/', views.partners, name="partners"),
    path('principles-foundations/', views.principles_foundations, name="principles-foundations"),
    path('program', views.program, name="program"),
    path('technology-enablers/', views.technology_enablers, name="technology-enablers"),
    path('under-construction/', views.under_construction, name="under-construction"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    path('signup/', views.signup, name="signup"),
    path('internship/profile/', views.internship_profile, name="internship-profile"),
    path('upload-resume/', views.upload_resume, name="upload-resume"),
    path('delete-resume/', views.delete_resume, name="delete-resume"),
    path('save-profile/', views.save_profile, name="save-profile"),
    path('change-pass/', views.change_pass, name="change-pass"),
]
