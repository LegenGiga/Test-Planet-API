from django.shortcuts import redirect

from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from planet.serializers import PlanetSerializer
from planet.models import Planet

class PlanetView(ViewSet):
    serializer_class = PlanetSerializer
    queryset = Planet.objects.all()

    def list(self, request):
        planets = Planet.objects.all()
        serializer = PlanetSerializer(planets, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = PlanetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()