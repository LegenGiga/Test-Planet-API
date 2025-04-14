from rest_framework import serializers
from planet.models import Planet

class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = '__all__'
