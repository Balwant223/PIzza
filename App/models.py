from django.db import models

class Pizza(models.Model):
    Type_choices=(
        ('regular','Regular'),
        ('square','Square'),
        )
    Type=models.CharField(max_length=50,choices=Type_choices,default='Regular')
    Size=models.CharField(max_length=50)
    Topping=models.CharField(max_length=50)