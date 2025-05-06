from tickit.models import Item, ItemList
from rest_framework import serializers


class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemList
        fields = ["id", "name"]


class ItemSerializer(serializers.ModelSerializer):
    item_list_details = ItemListSerializer(source="item_list", read_only=True)

    class Meta:
        model = Item
        fields = ["id", "text", "is_completed", "item_list", "item_list_details"]
