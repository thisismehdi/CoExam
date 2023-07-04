from django.forms import ModelForm
from .models import User, StudentProfile, TeacherProfile
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class StudentForm(ModelForm):
    class Meta:
        model = StudentProfile
        exclude = ('user',)
class TeacherForm(ModelForm):
    class Meta:
        model = TeacherProfile
        exclude = ('user',)

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','password1','password2',)


