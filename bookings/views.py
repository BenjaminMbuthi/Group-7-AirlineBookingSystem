from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import Flight, Passenger
from .serializers import FlightSerializer, PassengerSerializer

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    filter_backends = [SearchFilter]  # Enable filtering
    search_fields = ['origin', 'destination']  # Allow filtering by these fields

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    filter_backends = [SearchFilter]  # Enable filtering
    search_fields = ['flight__flight_number']  # Allow filtering passengers by flight number
