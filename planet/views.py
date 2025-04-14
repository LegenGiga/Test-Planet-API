from django.shortcuts import redirect

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from planet.serializers import PlanetSerializer
from planet.models import Planet

class PlanetView(ModelViewSet):
    serializer_class = PlanetSerializer
    queryset = Planet.objects.all()
