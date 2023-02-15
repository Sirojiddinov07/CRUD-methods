from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('student', StudentView, name='student'),
    path('delete-student/<int:pk>/', DeleteStudent, name='delete-student'),
    path('change-student/<int:pk>/', changeStudent, name='change-student'),
    path('delete-group/<int:pk>/', DeleteGroup, name='delete-group')


]
