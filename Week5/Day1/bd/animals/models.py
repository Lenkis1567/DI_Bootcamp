from django.db import models

class Family(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Animals(models.Model):
    name=models.CharField(max_length=50)
    legs=models.IntegerField()
    weight=models.FloatField()
    height=models.FloatField()
    speed=models.FloatField()
    family=models.ForeignKey(Family, on_delete=models.SET_NULL, null=True)
    url=models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Post(models.Model):
        title=models.CharField()

    def __str__(self):
        print(self.title)    
        

