from django.urls import path
import main_app.views as views

urlpatterns = [
    path('', views.index, name="index"),
    path('committee.html', views.committee, name="committee"),
    path('core_course.html', views.core_course, name="core_course"),
    path('faculty.html', views.faculty, name="faculty"),
    path('internship_postings.html', views.internship_postings, name="internship_postings"),
    path('partners.html', views.partners, name="partners"),
    path('principles_foundations.html', views.principles_foundations, name="principles_foundations"),
    path('program.html', views.program, name="program"),
    path('technology_enablers.html', views.technology_enablers, name="technology_enablers"),
    path('under_construction.html', views.under_construction, name="under_construction"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup")
]
