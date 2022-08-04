from django.db import models

# Create your models here.
class Student(models.Model):
    student_number = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    gpa = models.FloatField()

    def __str__(self) -> str:
        return f"Students: {self.first_name} {self.last_name}"