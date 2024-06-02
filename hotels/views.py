from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from .models import Hotels
from .serializers import HotelsSerializer, HotelsSerializerImageOne
from django.conf import settings
import time


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def register_hotels(request):
    # Extract data from request body
    city = request.data.get('city')
    hotelname = request.data.get('hotelname')
    address = request.data.get('address')
    price = request.data.get('price')
    first_image = request.FILES.get('first_image')
    time.sleep(5)
    second_image = request.FILES.get('second_image')
    third_image = request.FILES.get('third_image')
    fourth_image = request.FILES.get('fourth_image')
    stars = request.data.get('stars')
    description = request.data.get('description')

    print("Second Image:", second_image)
    print("Third Image:", third_image)
    print("Fourth Image:", fourth_image)

    # Create an instance of the Hotels model with the provided data
    hotel = Hotels.objects.create(
        city=city,
        hotelname=hotelname,
        address=address,
        price=price,
        first_image=first_image,
        second_image=second_image,
        third_image=third_image,
        fourth_image=fourth_image,
        stars=stars,
        description=description
    )

    # Serialize the created hotel object
    serializer = HotelsSerializer(hotel)

    return Response(serializer.data, status=201)

@api_view(['GET'])
def list_hotels(request):
    if request.method == 'GET':
        # Obtener todos los registros de la base de datos
        hoteles = Hotels.objects.all()

        # Crear una instancia del serializador y pasar los objetos obtenidos
        serializer = HotelsSerializer(hoteles, many=True)

        # Devolver una respuesta en formato JSON con los datos serializados
        return Response(serializer.data)

@api_view(['GET'])
def list_hotels_city(request, city):
    # Obtener todos los registros de la base de datos
    hotel = Hotels.objects.filter(city=city)

    # Crear una instancia del serializador y pasar los objetos obtenidos
    serializer = HotelsSerializer(hotel, many=True)

    # Devolver una respuesta en formato JSON con los datos serializados
    return Response(serializer.data)

@api_view(['GET'])
def list_hotels_id_url(request, id):
    # Obtener todos los registros de la base de datos
    hotel = Hotels.objects.filter(id=id)
    print("First Image:", hotel)
    # Crear una instancia del serializador y pasar los objetos obtenidos
    serializer = HotelsSerializerImageOne(hotel, many=True)

    # Devolver una respuesta en formato JSON con los datos serializados
    return Response(serializer.data)