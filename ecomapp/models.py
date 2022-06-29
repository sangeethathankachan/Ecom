from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User


class customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField (max_length=50)
    phone = models.CharField(max_length=10)
    email=models.EmailField()
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.firstname

class category(models.Model):
    categoryname=models.CharField(max_length=225)
    def __str__(self):
        return self.categoryname
    
    
class product(models.Model):
    category=models.ForeignKey(category,on_delete=models.CASCADE,blank=True,null=True)
    image=models.ImageField(upload_to='image/',null=True,blank=True)
    name=models.CharField(max_length=25)
    price=models.IntegerField()
    def __str__(self):
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey('product',
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField (max_length=50, default='', blank=True)
    phone = models.CharField (max_length=50, default='', blank=True)
    # date = models.DateField (default=datetime.datetime.today)
    status = models.BooleanField (default=False)
    
class cart(models.Model):
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    