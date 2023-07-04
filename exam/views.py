from json.encoder import JSONEncoder
from django.conf.urls import url
from django.contrib import messages
from django.http import request
from exam.models import Exam, Question,Note
from account.models import StudentProfile, TeacherProfile,User, create_profile
from django.http.response import HttpResponse, JsonResponse
from exam.forms import ExamForm, QuestionForm
from django.shortcuts import redirect, render
from rest_framework import generics
from django.urls import reverse
from .serializers import ExamSerializer
import random


# Create your views here.

def generateCode(length):
    caracters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    password = ''
    while length:
        upper = random.choice([True, False])
        if upper:
            char = random.choice(caracters)
            if not char.isdigit():
                password += char.upper()
            else:
                password += random.choice(caracters)
        else:
            password += random.choice(caracters)
        length = length - 1
        
    return password
def createExam(request):
    if request.method == 'POST':
        examCode = ''
        while True:
            code = generateCode(14)
            if not Exam.objects.filter(code=examCode).exists():
                break;
        name_exam = request.POST['exam']
        if len(name_exam):
            if not Exam.objects.filter(title=name_exam).exists():
                teacher = TeacherProfile.objects.get(user=request.user)
                exam = Exam.objects.create(title=name_exam,creator=teacher,code=code)
                exam.save()
                return render(request,'exam/createquestion.html',{'idexam':exam.id})
            else:
                messages.error(request,'ce nom existe déjà')
                return render(request,'exam/createexam.html')
        else:
            messages.error(request,'vous avez entrée un nom vide')
            return render(request,'exam/createexam.html')
    else:
        return render(request,'exam/createexam.html')


def createQuestion(request,idexam):
    if request.method =='POST':
        question = request.POST['question']
        A = request.POST['A']
        B = request.POST['B']
        C = request.POST['C']
        D = request.POST['D']
        answer = request.POST['answer']
        exam = Exam.objects.get(id=idexam)
        if len(A) and len(B) and len(C) and len(D):
            question=Question.objects.create(exam=exam,question=question,ch1=A,ch2=B,ch3=C,ch4=D,correct=answer)
            question.save()
            return render(request,'exam/createquestion.html',{'idexam':idexam,'qCount':Question.objects.filter(exam=exam).count})
        else:
            messages.error("You've entered an empty field !")
            return redirect('loginuser')
    else:
        return render(request,'exam/createexam.html')

def createQ(request,idexam):
    if request.method =="POST":
        name = Exam.objects.get(pk=idexam).title
        # here add the question
        question = request.POST['question']
        A = request.POST['answerA']
        B = request.POST['answerB']
        C = request.POST['answerC']
        D = request.POST['answerD']
        answer = request.POST['correctAnswer']
        exam = Exam.objects.get(id=idexam)
        if len(A) and len(B) and len(C) and len(D):
            question=Question.objects.create(exam=exam,question=question,ch1=A,ch2=B,ch3=C,ch4=D,correct=answer)
            question.save()
            count = Question.objects.filter(exam=exam).count()
        return JsonResponse({'succes':'message recieved succesfully','idexam':idexam,'count':count})

def cancel_exam(request,idexam):
    if request.is_ajax():
        exam = Exam.objects.get(id=idexam)
        exam.delete()
        return JsonResponse({"message":'exam deleted succesfully'})

def cancelExam(request,idexam):
    exam = Exam.objects.get(id=idexam)
    exam.delete()
    return redirect('home')

class QuestionList(generics.ListAPIView):
    serializer_class = ExamSerializer

    def get_queryset(self):
        exam = Exam.objects.get(id=self.kwargs['idexam'])
        questions = Question.objects.filter(exam=exam)
        return questions

# this function is for geting exams
def get_exam(request,pk):
    if request.method =="GET":
        exam = Exam.objects.get(id=pk)
        questions = Question.objects.filter(exam=exam)
        list = []
        for question in questions:
            obj = {
                'question':question.question,
                'a':question.ch1,
                'b':question.ch2,
                'c':question.ch3,
                'd':question.ch4,
                'correct':question.correct
            }
            list.append(obj)
        studentid = StudentProfile.objects.get(user=request.user).pk
        imageUrl = StudentProfile.objects.get(user=request.user).image
        return JsonResponse({'data':list,'studentid':studentid})


# la view responsable d'afficher la list des exam pour un prof
def listDesExams(request):
    user = request.user
    teacher = TeacherProfile.objects.get(user=user)
    exams = Exam.objects.filter(creator=teacher)
    context = {"exams":exams}
    return render(request,'exam/listDesExams.html',context)

def listDesNotes(request):
    etudiant = StudentProfile.objects.get(user=request.user)
    notes = Note.objects.filter(etudiant=etudiant)
    context = {"notes":notes}
    return render(request,'note/listDesNotes.html',context)

def EntrerCode(request):
    return render(request,'exam/enterCodeExam.html')

def getExam(request):
    if request.method == "POST":
        examCode = request.POST["code"]
        if not Exam.objects.filter(code=examCode).exists():
            return HttpResponse(f'<h2>Aucun Examen avec cette code: {examCode}</h2><a href="http://127.0.0.1:8000/">return<a/>')
        else:
            idExam = Exam.objects.get(code=examCode).id
            imageUrl = StudentProfile.objects.get(user=request.user).image
            name = StudentProfile.objects.get(user=request.user).__str__()
            idStudent = StudentProfile.objects.get(user=request.user).pk
            return render(request,'exam/passerExam.html',{'code':idExam,'imageUrl':imageUrl,'name':name,'idStudent':idStudent})
    return HttpResponse(f'no get requetst a sat')

def creerNote(request):
    if request.method=="POST":
        idExam = request.POST['idExam']
        idStudent = request.POST['idStudent']
        note = float(request.POST['note'])
        exam = Exam.objects.get(pk=idExam)
        student = StudentProfile.objects.get(pk=idStudent)
        if not Note.objects.filter(exam=exam,etudiant=student).exists():
            myNote = Note.objects.create(exam=exam,etudiant=student,note=note*20)
            myNote.save()
            return JsonResponse({'data':'succes'})
def bodyExam(request,pk):
    name = Exam.objects.get(pk=pk).title
    code = Exam.objects.get(pk=pk).code
    context = {'examId':pk,'examName':name,'examCode':code}
    return render(request,'exam/examBody.html',context)
        