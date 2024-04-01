from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="base/uploads/projects",null=True)
    def __str__(self):
        return self.name
    
class Client(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="base/uploads/clients",null=True)
    def __str__(self):
        return self.name