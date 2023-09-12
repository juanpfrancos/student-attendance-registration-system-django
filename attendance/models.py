# attendance/models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    # Otros campos de estudiante según tus necesidades

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    attended = models.BooleanField(default=False)
