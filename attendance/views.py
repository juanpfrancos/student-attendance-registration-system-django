from django.shortcuts import render, redirect
from .models import Student, Attendance
from django.http import JsonResponse

def student_list(request):
    students = Student.objects.all()
    return render(request, 'attendance/student_list.html', {'students': students})

def attendance_form(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        selected_students = request.POST.getlist('students')
        for student_id in selected_students:
            student = Student.objects.get(id=student_id)
            attendance = Attendance(student=student, date=date, attended=True)
            attendance.save()
        return JsonResponse({'message': 'Attendance saved successfully'})
    students = Student.objects.all()
    return render(request, 'attendance/attendance_form.html', {'students': students})

def filter_attendance(request):
    if request.method == 'GET':
        selected_date = request.GET.get('date')
        filtered_attendance = Attendance.objects.filter(date=selected_date)
        return render(request, 'attendance/filter_attendance.html', {'filtered_attendance': filtered_attendance, 'selected_date': selected_date})

def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        birthday = request.POST.get('birthday')
        Student.objects.create(name=name, date_of_birth=birthday)
        return redirect('/')
    return render(request, 'attendance/add_student.html')