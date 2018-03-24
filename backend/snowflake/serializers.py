from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from snowflake import models


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = '__all__'


class FridgeSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.Fridge
        fields = '__all__'

    items = ItemSerializer(many=True)
