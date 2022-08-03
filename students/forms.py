from tkinter import Widget
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_number', 'first_name', 'last_name', 'field_of_study', 'gpa']

        labels = {
            'student_number': 'Matric Number',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'field_of_study': 'Course of study',
            'gpa': 'GPA',
        }

        Widgets = {
            'student_number':forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'field_of_study': forms.TextInput(attrs={'class': 'form-control'}),
            'gpa': forms.NumberInput(attrs={'class': 'form-control'})
        }
