from tickit.models import Item, ItemList
from tickit.serializers import ItemSerializer, ItemListSerializer, ItemOrderSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class ItemListViewSet(viewsets.ModelViewSet):
    queryset = ItemList.objects.all()
    serializer_class = ItemListSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    @action(detail=True, methods=["put"], name="reorder")
    def reorder(self, request, *args, **kwargs):
        serializer = ItemOrderSerializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response(serializer.errors)

        new_order = request.data.get("order")
        item_being_reordered = self.get_object()
        item_list = item_being_reordered.item_list
        current_order = item_being_reordered.order

        adjustment = 0
        items_to_reorder = self.queryset.none()

        if new_order > current_order:
            items_to_reorder = self.queryset.all().filter(
                item_list=item_list, order__lte=new_order, order__gt=current_order
            )
            adjustment = -1

        elif new_order < current_order:
            items_to_reorder = self.queryset.all().filter(
                item_list=item_list, order__gte=new_order, order__lt=current_order
            )
            adjustment = 1

        for item in items_to_reorder:
            item.order += adjustment
            item.save()

        item_being_reordered.order = new_order
        item_being_reordered.save()

        return Response({"status": "items reordered"})
