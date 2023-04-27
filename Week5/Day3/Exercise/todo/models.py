from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=200)
    image=models.URLField(blank = True, null = True)

    def __str__(self):
        return self.name

class Todo(models.Model):
    title=models.CharField(max_length=100, blank =False)
    details=models.CharField(max_length=50)
    done=models.BooleanField(default=False)
    date_creation=models.DateTimeField(auto_now=True)
    date_completion=models.DateTimeField(blank=True, null=True)
    deadline_date=models.DateTimeField()
    category=models.ForeignKey('Category', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.title} | {self.details} | {self.category} | {self.done} | {self.date_creation} | {self.date_completion} | {self.deadline_date}'
