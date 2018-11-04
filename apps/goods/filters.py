import django_filters
from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤
    """
    price_min = django_filters.NumberFilter(name='shop_price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(name='shop_price', lookup_expr='lte')
    name = django_filters.CharFilter(name='name', lookup_expr='icontains')  # 加'i'忽略大小写 ,模糊查询,类似sql中的like

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max', 'name']
