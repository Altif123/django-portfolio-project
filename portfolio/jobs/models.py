from django.db import models

# Create your models here.

class Job (models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=1000)
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.role

class Project (models.Model):
    where = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    languages = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
       
    def __str__(self):
        return self.name