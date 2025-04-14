from django.shortcuts import redirect

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from drf_spectacular.utils import extend_schema

from rest_framework_api_key.permissions import HasAPIKey

from planet.serializers import PlanetSerializer
from planet.models import Planet


class PlanetView(ModelViewSet):
    serializer_class = PlanetSerializer
    queryset = Planet.objects.all()
    permission_classes = [HasAPIKey]
