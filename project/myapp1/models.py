from django.db import models

# Create your models here.

class Snippets(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    rmail = models.EmailField(max_length=30, blank=True, default='')
    
    def __str__(self):
        return self.name
