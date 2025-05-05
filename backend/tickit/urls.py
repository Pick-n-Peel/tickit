from django.contrib import admin
from django.urls import path, include
from tickit import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'list', views.ItemListViewSet, basename='list')
router.register(r'item', views.ItemViewSet, basename='item')

urlpatterns = router.urls