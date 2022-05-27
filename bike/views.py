from rest_framework import generics
from .models import Bike
from .serializers import BikeSerializer

class BikeList(generics.ListCreateAPIView):
  queryset = Bike.objects.all()
  serializer_class = BikeSerializer

class BikeDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Bike.objects.all()
  serializer_class = BikeSerializer
