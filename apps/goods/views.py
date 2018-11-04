from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import GoodsSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from .models import Goods
from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins
from rest_framework import viewsets
from .filters import GoodsFilter


# class GoodsListView(APIView):
#     def get(self,request,format=None):
#         goods = Goods.objects.all()[:10]
#         json_data = GoodsSerializer(goods,many=True)
#         return Response(json_data.data)


class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表页
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend,)
    filter_class = GoodsFilter
