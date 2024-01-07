from django.db import models

# Create your models here.

# super user username : project_relation
# super user password : abc

# This is one to one relations
class Person1(models.Model):
    name = models.CharField(max_length=100,null=True)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class AdharCard(models.Model):
    adhar_no = models.BigIntegerField(null=True,unique=True)
    person1 = models.OneToOneField(Person1,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.adhar_no)


# One to Many relations

class Person2(models.Model):
    name = models.CharField(max_length=100,null=True)
    age = models.IntegerField(null=True)

    def __str__(self):
        return str(self.name)

class Cars(models.Model):
    carName = models.CharField(max_length=100,null=True)
    person2 = models.ForeignKey(Person2,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.carName)

# Many to Many Relations

class Students(models.Model):
    name = models.CharField(max_length= 100,null=True)

    def __str__(self):
        return str(self.name)

class Book(models.Model):
    book_name = models.CharField(max_length=100,null=True)
    students = models.ManyToManyField(Students,null=True)

    def __str__(self):
        return str(self.book_name)

    