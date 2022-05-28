from distutils.command.upload import upload
from tkinter import CASCADE
from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=30)


    def save_locaton(self):
        self.save()




    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)


    def save_category(self):
        self.save()


    def __str__(self):
        return self.name



class Image(models.Model):
    image = models.ImageField(upload_to = 'pictures/')
    name = models.CharField(max_length=60)
    description = models.TextField()
    location = models.ForeignKey(Location,on_delete=CASCADE)


    def save_image(self):
        self.save()


    def __str__(self):
        return self.name + self.description


