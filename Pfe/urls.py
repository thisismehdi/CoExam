"""Pfe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Pfe import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from account import views
from exam.views import EntrerCode, bodyExam, cancelExam, createExam,createQuestion,QuestionList,createQ,cancel_exam, creerNote,get_exam,listDesExams,listDesNotes,getExam
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('',views.home,name="home"),
    path('signup/',views.signupuser,name='signupuser'),
    path('login/',views.loginuser,name='loginuser'),
    path('signup/student',views.studentreg,name='studentreg'),
    path('signup/teacher', views.teacherreg, name='teacherreg'),
    path('logout',views.logoutuser,name="logoutuser"),
    path('createexam',createExam,name="createExam"),# this url for creating exams
    path('createexam/<int:idexam>',createQuestion,name='createQuestion'),# this url for creating questions
    path('createQuestion/<int:idexam>',createQ),
    path('cancel-exam/<int:idexam>',cancel_exam),
    path('cancel/',cancelExam,name='cancel'),
    path('api/exam/<int:idexam>',QuestionList.as_view()), # this is the for exam api
    path('get-exam/<int:pk>',get_exam),
    path('listDesExams/',listDesExams,name='listDesExams'),
    path('listDesNotes/',listDesNotes,name='listDesNotes'),
    path('enterCodeExam/',EntrerCode,name="enterCode"),
    path('passerExam/',getExam,name='passerExam'),
    path('creerNote/',creerNote,name='creerNote'),
    path('exam/<int:pk>',bodyExam,name="exam")
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
