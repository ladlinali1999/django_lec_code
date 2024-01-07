from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    salary = models.FloatField(null=True)
    city = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.name}{self.age}{self.salary}{self.city}'
