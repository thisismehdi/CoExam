from django.forms import ModelForm
from .models import Exam, Question
class ExamForm(ModelForm):
    class Meta:
        model = Exam
        exclude = ('creator',)

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        exclude = ('exam',)