from django.contrib import admin
from .models import Student, Teacher, Department, Subject
# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Department)
admin.site.register(Subject)


