from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.forms.formsets import formset_factory

# Create your views here.
from datetime import datetime
from attendance.forms import CustomUserCreationForm, CreateClassroom, CreateStudent, AttendanceForm
from attendance.models import Classroom, Teacher, Student, Absence
from schools import settings


def home(request):
    return render(request, 'home.html')


def profile(request):
    if not request.user.is_authenticated():
        return redirect("login")
    classrooms = Classroom.objects.all()
    data = {
        'classrooms': classrooms
    }

    return render(request, 'profile.html', data)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = CustomUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })


@login_required
def new_classroom(request):
    if request.method == "POST":
        form = CreateClassroom(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            teacher = request.user
            classroom = Classroom.objects.create(name=name, teacher=teacher)
            return redirect("profile")
    else:
        form = CreateClassroom()
    # classrooms = Teacher.objects.filter(teacher=request.user)

    data = {'form': form}
    return render(request, 'new_classrooms.html', data)


def view_classroom(request, classroom_id):
    classroom = Classroom.objects.get(id=classroom_id)
    students = classroom.students.all()
    data = {'classroom': classroom, 'students': students}
    return render(request, "view_classroom.html", data)


def new_student(request):
    if request.method == "POST":
        form=CreateStudent(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("profile")
            # name = form.cleaned_data['name']
            # parent_phone = form.cleaned_data['parent_phone']
            # parent_email = form.cleaned_data['parent_email']
            # classroom = Classroom.objects.get(id=classroom_id)
            # student = Student.objects.create(name=name, parent_phone=parent_phone, parent_email=parent_email, classrooms=classroom)
            # return redirect("profile")
    else:
        form = CreateStudent()

    data = {'form': form}
    return render(request, 'new_student.html', data)


def view_student(request, student_id):
    student = Student.objects.get(id=student_id)
    classrooms = student.classrooms.all()
    absences = student.absences.all().count()
    data = {'student': student, 'classrooms': classrooms, 'absences': absences}
    return render(request, 'view_student.html', data)


def take_attendance(request, classroom_id):
    if request.method == "POST":
        form = AttendanceForm()
        students = request.POST.getlist('students')[:-1]
        for student in students:
            classroom = Classroom.objects.get(id=classroom_id)
            student_obj=Student.objects.get(id=int(student))
            date = datetime.today()
            absent=True
            Absence.objects.create(classroom=classroom, date=date, student=student_obj, absent=absent)
            if student_obj.absences.all().count() ==3:
                text_content = 'Your student has 3 absences'
                html_content = '<p>Your student {} has missed 3 days of class!'.format(student_obj.name)
                msg = EmailMultiAlternatives("Student absences", text_content, settings.DEFAULT_FROM_EMAIL, [student_obj.parent_email])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
        return redirect('profile')

    else:
        form=AttendanceForm()

    classroom = Classroom.objects.get(id=classroom_id)
    data = {'form': form, 'classroom': classroom}
    return render(request, 'take_attendance.html', data)


















