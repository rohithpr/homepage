from rest_framework import serializers
from rest_framework_json_api.views import ModelViewSet

from .models import Collection, Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "key", "value", "kind", "row", "collection"]


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["key", "column", "row", "id"]


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
