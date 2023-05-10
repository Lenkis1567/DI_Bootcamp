from django.db import models
from rest_framework import permissions

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    admin = models.OneToOneField('auth.User', related_query_name='user', on_delete=models.CASCADE, null=True)
    def __str___(self):
        return f'{self.name} {self.description}'
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str___(self):
        return f'{self.name}'

class Project(models.Model):
   
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    employ = models.ManyToManyField(Employee, related_name='empl')
    def __str___(self):
        return f'{self.name} {self.description} {self.start_date} {self.end_date} {self.employ.empl.name}'

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    def __str___(self):
        return f'{self.name} {self.description}{self.due_date} {self.completed}'
