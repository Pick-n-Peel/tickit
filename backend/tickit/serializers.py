from tickit.models import Item, ItemList
from rest_framework import serializers

class ItemListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=30, required=True)

    class Meta:
        model = ItemList
        fields = ['id', 'name']


class ItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField(max_length=100, required=True)
    is_completed = serializers.BooleanField(default=False)
    item_list = serializers.PrimaryKeyRelatedField(queryset=ItemList.objects.all())
    item_list_details = ItemListSerializer(source='item_list', read_only=True)

    class Meta:
        model = Item
        fields = ['id', 'text','is_completed','item_list', 'item_list_details']
