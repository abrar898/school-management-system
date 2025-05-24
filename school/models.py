from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    phone = models.CharField(max_length=10)
    image=models.ImageField(upload_to='students/',null=True,blank=True)
    
    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    phone = models.CharField(max_length=10)
    image=models.ImageField(upload_to='teachers/',null=True,blank=True)
    
    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Subject(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name









