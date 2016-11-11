from django.db import models

# Create your models here.

class Student(models.Model):
    enrollment_number = models.CharField(max_length=15, unique=True)
    name = models.TextField()
    course = models.CharField(max_length=20)
    dob = models.DateTimeField(blank=True, null=True)
    

    def __str__(self):
        return self.name
