from django.db import models
from django.db.models.deletion import CASCADE

class List(models.Model):
    pass 

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(default=None, to=List, on_delete=models.CASCADE)