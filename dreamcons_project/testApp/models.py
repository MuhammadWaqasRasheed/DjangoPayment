from django.db import models

# Create your models here.
"""
class Project(models.Model):
    title=models.CharField(max_length=50, verbose_name="Title")
    description=models.CharField(max_length=1000 ,verbose_name="Description")
    client_name=models.CharField(max_length=1000 ,verbose_name="Description")

class Task(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title")
    description = models.CharField(max_length=1000, verbose_name="Description")
    time_elapsed = models.IntegerField(verbose_name="Elapsed time" ,null=True, default=None, blank=True)
    importance = models.IntegerField(verbose_name="Importance")
    project = models.ForeignKey(Project, verbose_name="Project" ,null=True, default=None, blank=True,on_delete=models.CASCADE)
    #app_user = models.ForeignKey(UserProfile, verbose_name="User")
"""

#Implementing many to many Relationship

class Topping(models.Model):
    toppingName=models.CharField(max_length=20)

    def __str__(self):
        return self.toppingName
    

class Pizza(models.Model):
    pizzaName=models.CharField(max_length=20)
    price=models.IntegerField()
    toppings=models.ManyToManyField(Topping)

#Foreign key example
class Manufacturer(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Car(models.Model):
    name=models.CharField(max_length=20)
    manufacturer=models.ForeignKey(Manufacturer,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
#below here is Many to Many Field Exmaple
class Person(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')
    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)
    invite_reason = models.CharField(max_length=64)

    def __str__(self):
        return self.invite_reason