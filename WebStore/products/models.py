from django.db import models


#inheriting class Model from models
#this class has all common operations we have to use in models
class Product(models.Model):
    #we define max_length so it wont get hacked or crashed
    name = models.CharField(max_length=255) #CharFiled field that can contain textual data
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083) #standard max length for urls

class Offer(models.Model):
    code = models.CharField(max_length= 10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
