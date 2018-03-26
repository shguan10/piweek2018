from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from snowflake import models


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = ['name', 'date_entered']


class FridgeSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.Fridge
        fields = ['id', 'items']

    items = ItemSerializer(many=True)
