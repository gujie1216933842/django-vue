from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import GoodsSerializer

from .models import Goods

class GoodsListView(APIView):
    def get(self,request,format=None):
        goods = Goods.objects.all()[:10]
        json_data = GoodsSerializer(goods,many=True)
        return Response(json_data.data)


