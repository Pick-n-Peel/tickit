from tickit import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'list', views.ItemListViewSet, basename='list')
router.register(r'item', views.ItemViewSet, basename='item')

urlpatterns = router.urls
