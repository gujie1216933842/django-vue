import json
from django.views.generic.base import View
from goods.models import Goods
from django.http import HttpResponse, JsonResponse
from django.core import serializers


class GoodsListView(View):
    def get(self, request):
        """
        通过django的view实现商品的列表页
        :param request:
        :return:
        """
        goods = Goods.objects.all()[:10]
        json_data = serializers.serialize('json', goods)
        json_data = json.loads(json_data)

        return JsonResponse(json_data)
