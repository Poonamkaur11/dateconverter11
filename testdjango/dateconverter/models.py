from django.db import models

# Create your models here.



class DateFunctionMap(models.Model):
    input_string = models.CharField(max_length=100)
    related_function_name = models.CharField(max_length=100)

