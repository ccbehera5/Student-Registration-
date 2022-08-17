from django.db import models

# Create your models here.
class StudentData(models.Model):
    Name=models.CharField(max_length=100)
    Department=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Mobile=models.BigIntegerField()
    Address=models.CharField(max_length=100)
