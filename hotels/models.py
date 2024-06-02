from django.db import models

# Create models hotels.
class Hotels (models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50)
    hotelname = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=20, decimal_places=5)
    first_image = models.ImageField(upload_to = 'images/')
    second_image = models.ImageField(upload_to = 'images/')
    third_image = models.ImageField(upload_to = 'images/')
    fourth_image = models.ImageField(upload_to = 'images/')
    stars = models.IntegerField()
    description = models.CharField(max_length=1000)
