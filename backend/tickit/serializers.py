from tickit.models import Item, ItemList
from rest_framework import serializers


class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemList
        fields = ["id", "name"]


class ItemSerializer(serializers.ModelSerializer):
    order = serializers.IntegerField(read_only=True)

    class Meta:
        model = Item
        fields = ["id", "text", "is_completed", "item_list", "order"]

    def create(self, validated_data):
        item_list = validated_data["item_list"]
        validated_data["order"] = Item.objects.filter(item_list=item_list).count()
        return super().create(validated_data)


class ItemOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["order"]
