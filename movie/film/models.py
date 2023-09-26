from django.db import models

class Film(models.Model):
    name=models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='film/img', null=True, blank=True)
    director=models.CharField(max_length=30)
    writer=models.CharField(max_length=30)
    Starring=models.CharField(max_length=100)
    release_year=models.IntegerField()
    running_time=models.CharField(max_length=20)