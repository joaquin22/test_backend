from django.db import models


class CustomUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Product(models.Model):
    name = models.CharField(max_length=100)
