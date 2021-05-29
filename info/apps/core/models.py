from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    search_term = models.TextField(max_length=2000)
    product = models.CharField(max_length=200)
    price = models.TextField(max_length=2000)
    image = models.TextField(max_length=2000)
    link = models.TextField(max_length=2000)

    class Meta:
        db_table = 'post'

    def __str__(self):
        return self.search_term
