from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    email = models.EmailField()
    date_joined = models.DateTimeField()

    def __str___(self):
        return f'{self.first_name} {self.last_name} {self.email}'
