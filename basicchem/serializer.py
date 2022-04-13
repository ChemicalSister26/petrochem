from rest_framework import serializers

from .models import Basicchem


class BasicchemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basicchem
        fields = "__all__"

    # title = serializers.CharField(max_length=255)
    # content = serializers.CharField()
    # slug = serializers.CharField()
    # time_create = serializers.DateTimeField(read_only=True)
    # time_update = serializers.DateTimeField(read_only=True)
    # is_published = serializers.BooleanField(default=True)
    # cat_id = serializers.IntegerField()
    #
    # def create(self, validated_data):
    #     return Basicchem.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance)
    #     instance.content = validated_data.get('content', instance)
    #     instance.slug = validated_data.get('slug', instance)
    #     instance.time_update = validated_data.get('time_update', instance)
    #     instance.is_published = validated_data.get('is_published', instance)
    #     instance.cat_id = validated_data.get('cat_id', instance)
    #     instance.save()
    #
    #     return instance


