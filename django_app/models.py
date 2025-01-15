from django.db import models

# Create your models here.
class Car(models.Model):
    title = models.TextField(max_length=250)
    year = models.TextField(max_length=4, null=True)
    color = models.TextField(max_length=250, null=True)
    
    def __str__(self):
        return f"Marca: {self.title} -- Año: {self.year} -- Color: {self.color}"

class Publisher(models.Model):
    name = models.TextField(max_length=100)
    address = models.TextField(max_length=100)

    def __str__(self):
        return f"Publisher: {self.name}"
    
class Author(models.Model):
    name = models.TextField(max_length=100)
    
    def __str__(self):
        return f"Author: {self.name}"
    
class Book(models.Model):
    title = models.TextField(max_length=100)
    authors = models.ManyToManyField(Author)
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return f"Book: {self.title} -- Authors: {self.authors} -- Published: {self.publication_date}"
