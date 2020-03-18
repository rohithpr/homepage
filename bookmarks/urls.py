from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register("item", views.ItemViewSet)
router.register("collection", views.CollectionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
