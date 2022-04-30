from django.db import models

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=30,default="none")
    desc=models.CharField(max_length=300,default="")
    price=models.IntegerField(default="")
    sub=models.CharField(max_length=30,default="")
    pub_date=models.DateField(default="0000-00-00")
    image=models.ImageField(upload_to="shop/images",default="")



    def __str__(self):
        return self.product_name
from django.db import models

class Contact(models.Model):
    msg_id=models.AutoField
    fname=models.CharField(max_length=30,default='none')
    lname=models.CharField(max_length=20,default='none')
    email=models.CharField(max_length=300,default='')
    password=models.IntegerField(default='123')
    Address1=models.CharField(max_length=300,default='')
    Address2=models.CharField(max_length=500,default='')
    city=models.CharField(max_length=400,default='')
    pinc=models.IntegerField(default='')
    query=models.CharField(max_length=500,default='')



    def __str__(self):
        return self.fname

class Ordedr(models.Model):
    order_id=models.AutoField
    name=models.CharField(max_length=30,default='none')
    cnum=models.IntegerField(default='')
    email=models.CharField(max_length=300,default='')
    password=models.IntegerField(default='123')
    Address1=models.CharField(max_length=300,default='')
    Address2=models.CharField(max_length=500,default='')
    city=models.CharField(max_length=400,default='')
    pinc=models.IntegerField(default='')
    query=models.CharField(max_length=500,default='')



    def __str__(self):
        return self.name



