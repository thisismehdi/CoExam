from django import http
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SignupForm, StudentForm, TeacherForm
from .models import User,StudentProfile,TeacherProfile
import re
regexEmail = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
regexName = '[a-zA-Z]{3,30}'

def check_email(email):
    if re.search(regexEmail, email):
        return True
    return False

def isName(name):
    if re.match(r'^[aA-zZ]+$', name):
        return True
    return False
# Create your views here.
def signupuser(request):
    form = SignupForm()
    if request.method == 'POST':
        """form = SignupForm(request.POST)
        if form.is_valid():
            email = request.POST['email'] 
            password = request.POST['password1']
            User.objects.create_user(email,password,is_active=True)
            return HttpResponse('user created')
        else:
            return HttpResponse('user deja')"""
        form = SignupForm(request.POST)
        email = request.POST['email'] 
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if check_email(email) and password1 == password2 and not User.objects.filter(email=email).exists() and password2 !="":
            User.objects.create_user(email,password1,is_teacher=True)
            return HttpResponse('user created')
        else:
            return render(request, 'account/signup.html',{'form':form,"error":'this email is already exists'})

    return render(request, 'account/signup.html',{'form':form})
# we don't need this anymore
'''
def loginuser(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        #form = AuthenticationForm(data=request.POST) # dont forget data
    #if form.is_valid():
        #  have user sUARE BRACKETS AND TO GET METHOD AND THAT CAUSE ME AN ERROR
        # 'builtin_function_or_method' object is not subscriptable
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request,'account/login.html',{'form':form,"error":"user or password is wrong or"})
    #else:
        #return HttpResponse('dkxi li dakhalti maxi valid')
    return render(request,'account/login.html',{'form':form})
'''

def loginuser(request):
    if request.method =="POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request,user)
            return render(request,'index.html')
        else:
            messages.error(request,'email ou mot de passe est incorrect !')
            return redirect('loginuser')
    else:
        return render(request,'account/login.html')

def logoutuser(request):
    logout(request)
    return render(request,'index.html')
#####################################################################################
# create student account
def studentreg(request):
    if request.method == 'POST':
        image = request.FILES.get("image")
        data = request.POST
        first_name = data['first_name']
        second_name = data.get("second_name")
        email = data['email']
        cne = data['cne']
        password1 = data.get("password1")
        password2 = data.get("password2")
        if isName(first_name):
            # the first name is valid
            if isName(second_name):
                # the second name is valid
                if check_email(email):
                    # the email is valid
                    if not User.objects.filter(email=email).exists():
                        # the email is good
                        if len(cne) and not StudentProfile.objects.filter(cne=cne).exists():
                            # is valid cne
                            if password1==password2:
                                user=User.objects.create_user(email,password1,is_teacher=False)
                                student = StudentProfile.objects.get(user=user)
                                student.first_name = first_name
                                student.last_name = second_name
                                student.image = image
                                student.cne=cne
                                # don't forget to save
                                student.save()
                                messages.success(request,'compte crèè avec succès')
                                return redirect('loginuser')
                            else:
                                messages.error(request,'les mots de passe ne correspondent pas')
                                return render(request,'account/signupstudent.html')
                        else:
                            messages.error(request,"cne existe déjà")
                            
                    else:
                        messages.error(request,'email existe déjà')
                        return render(request,'account/signupstudent.html')
                else:
                    messages.error(request,'nom n\'est pas valid')
                    return render(request,'account/signupstudent.html')
            else:
                messages.error(request,'nom n\'est pas valid')
                return render(request,'account/signupstudent.html')
        else:
            messages.error(request,'prenom n\'est pas valid')
            return render(request,'account/signupstudent.html')
        
    else:
        return render(request,'account/signupstudent.html')
###################################################################################################
# create a teacher account
def teacherreg(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data['first_name']
        second_name = data.get("second_name")
        email = data['email']
        password1 = data.get("password1")
        password2 = data.get("password2")
        print(str(first_name))
        if isName(first_name):
            # the first name is valid
            if isName(second_name):
                # the second name is valid
                if check_email(email):
                    # the email is valid
                    if not User.objects.filter(email=email).exists():
                        # the email is good
                        print(password1)
                        if password1==password2:
                            user=User.objects.create_user(email,password1,is_teacher=True)
                            teacher = TeacherProfile.objects.get(user=user)
                            teacher.first_name = first_name
                            teacher.last_name = second_name
                            # don't forget to save
                            teacher.save()
                            return redirect('home')
                        else:
                            messages.error(request,'the passwords didn\'t matches')
                            return render(request,'account/signupteacher.html')
                    else:
                        messages.error(request,'this email is aleady exists in our database')
                        return render(request,'account/signupteacher.html')
                else:
                    messages.error(request,'the second name that you\'ve entred is invalid')
                    return render(request,'account/signupteacher.html')
            else:
                messages.error(request,'the second name that you\'ve entred is invalid')
                return render(request,'account/signupteacher.html')
        else:
            messages.error(request,'the first name that you\'ve entred is invalid')
            return render(request,'account/signupteacher.html')
    return render(request,'account/signupteacher.html')


def home(request):
    return render(request,'index.html')

