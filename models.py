#path: jSchool/jSchool
from django.db import models

class Student(models.Model):
    name = models.CharField(unique=True, max_length=50)
    pid = models.CharField(unique=True, max_length=12)
    grade = models.IntegerField(unique=False)
# same models.py, below the first model.

class Course(models.Model):
    name = models.CharField(max_length=50)
    call_number = models.CharField(unique=False, max_length=4)
    instructor = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    term = models.CharField(max_length=200)
    date = models.DateField()
