from exam.models import Question
from rest_framework import serializers
# this serializer is made for exam api
class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question', 'ch1', 'ch2', 'ch3', 'ch4', 'correct']