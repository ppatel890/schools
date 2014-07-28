from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Teacher(AbstractUser):
    phone = models.CharField(max_length=12, help_text="Format should be 111-111-1111")

    def __unicode__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Classroom(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, related_name='classrooms')

    def __unicode__(self):
        return "{}".format(self.name)


class Student(models.Model):
    name = models.CharField(max_length=100)
    parent_phone = models.CharField(max_length=12)
    parent_email = models.EmailField()
    classrooms = models.ManyToManyField(Classroom, related_name="students")

    def __unicode__(self):
        return "{}".format(self.name)


class Absence(models.Model):
    classroom = models.ForeignKey(Classroom)
    date = models.DateField()
    student = models.ForeignKey(Student, related_name="absences")
    absent = models.BooleanField(default=False)
