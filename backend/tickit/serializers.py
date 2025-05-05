from tickit.models import Item, ItemList
from rest_framework import serializers

class ItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField(max_length=100, required=True)
    is_completed = serializers.BooleanField(default=False)
    item_list = serializers.IntegerField(required=True)

    class Meta:
        model = Item
        fields = ['id', 'text','is_completed','item_list']


class ItemListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=30, required=True)

    class Meta:
        model = ItemList
        fields = ['id', 'name']



