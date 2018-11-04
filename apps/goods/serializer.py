from rest_framework import serializers
from .models import Goods,GoodsCategory,Banner,GoodsCategoryBrand


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = "__all__"
