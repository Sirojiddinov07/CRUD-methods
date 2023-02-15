from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Student(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.IntegerField()

