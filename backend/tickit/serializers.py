from tickit.models import Item, ItemList
from rest_framework import serializers


class OrderDefault:
    requires_context = True

    def __call__(self, serializer_field):
        data = serializer_field.context.get("request").data
        item_list = data.get("item_list")
        return Item.objects.all().filter(item_list=item_list).count()


class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemList
        fields = ["id", "name"]


class ItemSerializer(serializers.ModelSerializer):
    order = serializers.IntegerField(default=OrderDefault())

    class Meta:
        model = Item
        fields = ["id", "text", "is_completed", "item_list", "order"]
