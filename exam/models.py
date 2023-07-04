from django.db import models
from account.models import StudentProfile, TeacherProfile
# Create your models here.
# how exam class look in data base
class Exam(models.Model):
    title = models.CharField(max_length = 64)
    creator = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE,null=True)
    code =models.CharField(unique=True,max_length=64)
    def __str__(self):
        return self.title
    def nbrQuestions(self):
        return Exam.question_set.all().count

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE,null=True)
    question = models.CharField(max_length = 250,blank=True)
    ch1 = models.CharField(max_length=250,blank=True)
    ch2 = models.CharField(max_length=250,blank=True)
    ch3 = models.CharField(max_length=250,blank=True)
    ch4 = models.CharField(max_length=250,blank=True)
    correct = models.CharField(max_length=1,blank=True)

    def __str__(self):
        return self.question

class Note(models.Model):
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
    etudiant = models.ForeignKey(StudentProfile,on_delete=models.CASCADE)
    note = models.FloatField(default=0)
    def __str__(self):
        return self.etudiant.__str__()
    @property
    def nomEtudiant(self):
        return self.etudiant.__str__()
    @property
    def nomExam(self):
        return self.exam.title


