from django.db import models

class Gif(models.Model):
    title=models.CharField(max_length=100, blank =False)
    url=models.URLField()
    uploader_name=models.CharField (max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    likes=models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} | {self.url} | {self.uploader_name} | {self.created_at}'
    

class Category(models.Model):
    name = models.CharField(max_length=50)
    gifs=models.ManyToManyField(Gif, related_name='categories') 

    def __str__(self):
        return self.name


