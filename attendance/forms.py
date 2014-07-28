from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import  User
from django.forms import ModelForm, ModelChoiceField, ModelMultipleChoiceField
from attendance.models import Teacher, Classroom, Student, Absence
from django.forms.formsets import formset_factory, BaseFormSet


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=12)

    class Meta:
        model = Teacher
        fields = ("username", "email", "first_name", "last_name", "phone", "password1", "password2")

    def clean_username(self):
            # Since User.username is unique, this check is redundant,
            # but it sets a nicer error message than the ORM. See #13147.
            username = self.cleaned_data["username"]
            try:
                Teacher.objects.get(username=username)
            except Teacher.DoesNotExist:
                return username
            raise forms.ValidationError(
                self.error_messages['duplicate_username'],
                code='duplicate_username',
            )


class CreateClassroom(forms.Form):
    name = forms.CharField(max_length=100)


class CreateStudent(ModelForm):
    class Meta:
        model = Student
    # name = forms.CharField(max_length=100)
    # parent_phone = forms.CharField(max_length=12)
    # parent_email = forms.EmailField()


class AttendanceForm(forms.Form):

    class Meta:
        model = Absence

    def __init__(self):
        super(AttendanceForm, self).__init__()
        self.fields['students'] = ModelMultipleChoiceField(queryset=Student.objects.all(), widget=forms.CheckboxSelectMultiple)













