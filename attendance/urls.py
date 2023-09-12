# attendance/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('student_list/', views.student_list, name='student_list'),
    path('attendance_form/', views.attendance_form, name='attendance_form'),
    path('filter_attendance/', views.filter_attendance, name='filter_attendance'),
    path('add_student/', views.add_student, name='add_student'),
]
