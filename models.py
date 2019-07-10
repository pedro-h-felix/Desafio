from django.db import models
from .choices import *


class Produto(models.Model):

    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    tel = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True) 
    description = models.TextField()
    created_at = models.DateField('criado em', auto_now_add=True)
    image = models.ImageField(upload_to= ' pic_folder/', default='baseline-check_circle_outline.csv')
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    
    
    def __str__(self):
        return self.name

