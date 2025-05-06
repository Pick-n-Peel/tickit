from tickit.models import Item, ItemList
from tickit.serializers import ItemSerializer, ItemListSerializer
from rest_framework import viewsets

class ItemListViewSet(viewsets.ModelViewSet):
    queryset = ItemList.objects.all()
    serializer_class = ItemListSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
