# Django
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Restaurant(models.Model):
    id = models.TextField(primary_key=True)
    rating = models.IntegerField(validators=[MaxValueValidator(4), MinValueValidator(0)])
    name = models.TextField(max_length=200)
    site = models.TextField(max_length=50)
    email = models.TextField(max_length=50)
    phone = models.TextField(max_length=10)
    street = models.TextField(max_length=200)
    city = models.TextField(max_length=200)
    state = models.TextField(max_length=200)
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.name
