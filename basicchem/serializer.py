from rest_framework import serializers

from .models import Basicchem


class BasicchemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basicchem
        fields = '__all__'