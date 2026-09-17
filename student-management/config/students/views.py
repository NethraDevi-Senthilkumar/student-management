
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student


def home(request):
    students = Student.objects.all()
    return render(request, 'students/home.html', {'students': students})


def add_student(request):
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            course=request.POST['course'],
            age=request.POST['age']
        )
    return redirect('home')


def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.course = request.POST['course']
        student.age = request.POST['age']
        student.save()
        return redirect('home')

    return render(request, 'students/edit.html', {'student': student})


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('home')
# Create your views here.
