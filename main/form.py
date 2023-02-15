from django.forms import ModelForm
from .models import *



class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

