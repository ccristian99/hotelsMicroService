from rest_framework import serializers
from .models import Hotels

class HotelsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Hotels
        fields = ['id', 'city', 'hotelname', 'address', 'price', 'first_image', 'second_image', 'third_image', 'fourth_image','stars','description']

class HotelsSerializerImageOne(serializers.ModelSerializer):
    class Meta: 
        model = Hotels
        fields = ['first_image']
