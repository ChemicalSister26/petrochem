from rest_framework import serializers

from .models import Basicchem


class BasicchemSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Basicchem
        fields = '__all__'