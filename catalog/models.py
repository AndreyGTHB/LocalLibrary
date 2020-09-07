from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=50, help_text="Enter a book genre here")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100, help_text="Enter a book name here")
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a description of the book")
