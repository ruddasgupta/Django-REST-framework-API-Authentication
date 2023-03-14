from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')

    def __str__(self):
        return 'name: ' + self.name


class Book(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='genre')
    description = models.CharField(max_length=200, blank=False, default='')
    publisher = models.CharField(max_length=200, blank=False, default='')
    author = models.CharField(max_length=200, blank=False, default='')
    year = models.IntegerField(blank=False)

    def __str__(self):
        return {
            "title": self.title,
            "genre": self.genre.name,
            "description": self.description,
            "publisher": self.publisher,
            "author": self.author,
            "year": self.year
        }.__str__()
