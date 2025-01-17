from django.db import models

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

class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    website = models.URLField(max_length=250)
    biography = models.TextField(max_length=500)

class Book(models.Model):
    title = models.TextField(max_length=100)
    authors = models.ManyToManyField(Author, related_name="authors")
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return f"Book: {self.title} -- Author: {self.authors} -- Published: {self.publication_date} -- Publication Date: {self.publication_date}"