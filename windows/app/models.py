from django.urls import path
from django.db import models

class Window(models.Model):
    name = models.CharField(max_length=255)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Glass(models.Model):
    glass = models.CharField(max_length=255)
    text = models.TextField()
    total = models.IntegerField()
    window = models.ForeignKey(Window, on_delete=models.CASCADE)

    def __str__(self):
        return self.glass


