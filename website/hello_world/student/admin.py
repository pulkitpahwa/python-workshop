from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'enrollment_number', 'course')


admin.site.register(Student, StudentAdmin)

# Register your models here.
