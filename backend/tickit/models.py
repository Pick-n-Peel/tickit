from django.db import models


class ItemList(models.Model):
    name = models.CharField(max_length=30)


class Item(models.Model):
    text = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    item_list = models.ForeignKey(ItemList, on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField(default=0)
