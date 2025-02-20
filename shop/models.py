from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    Offer=models.IntegerField(default=0)
    product_name=models.CharField(max_length=20)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=20,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=100)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name
class Contact(models.Model):
    message_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    phone=models.IntegerField()
    message=models.CharField(max_length=300)
class Order(models.Model):
    order_name=models.CharField(max_length=20) 
    order_email=models.CharField(max_length=20,default="")
    order_phone=models.IntegerField()
    order_city=models.CharField(max_length=30)
    order_state=models.CharField(max_length=30)
    order_zip=models.CharField(max_length=7)

class UpdateOrder(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=5000)
    timestamp=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7]+"....."

class Buy(models.Model):
    buy_price=models.IntegerField(default=0)
