from django.db import models

# Create your models here.
# super user username and password
# username = project_orm
# password = abc


class Products(models.Model):
    pname = models.CharField(max_length=100,null=True)
    price = models.FloatField(null=True)
    desc = models.CharField(max_length=100,null=True)
    quantity = models.IntegerField(max_length=100,null=True)
