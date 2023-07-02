from django.db import models


# Create your models here.
class Book(models.Model):
    book_no = models.CharField(max_length=32, unique=True)
    book_name = models.CharField(max_length=32)
