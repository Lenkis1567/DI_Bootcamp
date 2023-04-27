from django.db import models

class Cathegory(models.Model):
    name=models.CharField(max_length=50)
    gifs=models.ManyToManyField('Gif') 

    def __str__(self):
        return self.name

class Gif(models.Model):
    title=models.CharField(max_length=100, blank =False)
    url=models.URLField(blank=True, null=True)
    uploader_name=models.CharField (max_length=100)
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} | {self.url} | {self.uploader_name} | {self.created_at}'

