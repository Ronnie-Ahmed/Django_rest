from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    description=models.TextField(max_length=10000)
    email=models.EmailField(max_length=30)
    
    def __str__(self):
        return self.name
    
    def get_discount(self):
        return "220"
    
