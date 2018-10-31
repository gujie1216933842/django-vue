from datetime import datetime
from DjangoUeditor.models import UEditorField
from django.db import models


# Create your models here.

# UEditorField

class GoodsCategory(models.Model):
    name = models.CharField()
    code = models.CharField()
    desc = models.CharField()
    category_type = models.CharField(choices=(()))
    parent_category = models.ForeignKey('self', null=True, verbose_name='父类别')
    is_tab = models.BooleanField(default=False)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '商品类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsCategoryBrand(models.Model):
    name = models.CharField(default='', max_length=30, verbose_name='品牌名', help_text='品牌名')
    desc = models.TextField(default='', max_length=200, verbose_name='品牌描述', help_text='品牌描述')
    image = models.ImageField(max_length=200, upload_to='brand/images/')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '品牌'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    '''商品'''
    category = models.ForeignKey(GoodsCategory, null=True, blank=True, verbose_name='商品类目')
    goods_sn = models.CharField(max_length=50, default='', verbose_name='商品唯一货号')
    name = models.IntegerField(max_length=300, verbose_name='商品名')
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    sold_num = models.IntegerField(default=0, verbose_name='商品销售量')
    fav_num = models.IntegerField(default=0, verbose_name='商品收藏量')
    goods_num = models.IntegerField(default=0, verbose_name='库存数')
    market_price = models.FloatField(default=0, verbose_name='市场价格')
    shop_price = models.FloatField(default=0, verbose_name='本店价格')
    goods_brief = models.CharField(max_length=500, verbose_name='商品简短描述')
    goods_desc = UEditorField(verbose_name=u'内容', imagepath='goods/images/', width=1000, )
    ship_free = models.BooleanField(default=True, verbose_name='是否包邮')
    goods_front_image = models.ImageField(upload_to='', null=True, blank=True, verbose_name='商品封面图片')
    goods_front_image_url = models.CharField(max_length=300, default='', verbose_name='商品封面图片地址')
    is_new = models.BooleanField(default=False, verbose_name='是否是新品')
    is_hot = models.BooleanField(default=False, verbose_name='是否是热销的商品')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name


class GoodsImage(models.Model):
    '''商品轮播图'''
    goods = models.ForeignKey(Goods, verbose_name='商品', related_name='images')
    image = models.ImageField(upload_to='', verbose_name='商品图片')
    image_url = models.CharField(max_length=300, null=True, blank=True, verbose_name='图片url')
    add_time = models.DateTimeField()

    class Meta:
        verbose_name = '商品轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    goods = models.ForeignKey(Goods, verbose_name='商品')
    image = models.ImageField(upload_to='banner', verbose_name='轮播图片')
    index = models.IntegerField(default=0, verbose_name='轮播顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '商品轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name
