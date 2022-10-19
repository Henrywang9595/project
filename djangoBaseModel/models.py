# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.
class KeHu(models.Model):
    ZhangHao = models.CharField(max_length=200,default='',verbose_name=u'账号')
    MiMa = models.CharField(max_length=200,default='',verbose_name=u'密码')
    YongHuMing = models.CharField(max_length=200,default='',verbose_name=u'用户名')
    XingBie = models.CharField(max_length=200,default='',verbose_name=u'性别')
    NianLing = models.CharField(max_length=200,default='',verbose_name=u'年龄')
    TouXiang = models.CharField(max_length=200,default='',verbose_name=u'头像')
    createtime = models.DateTimeField("创建时间",auto_now_add=True)#自动添加时间
    class Meta:
        verbose_name_plural = '客户列表'
    def __str__(self):
        return self.ZhangHao

class YongHu(models.Model):
    ZhangHao = models.CharField(max_length=200,default='',verbose_name=u'账号',unique=True)
    MiMa = models.CharField(max_length=200,default='',verbose_name=u'密码')
    XingMing = models.CharField(max_length=200,default='',verbose_name=u'姓名')
    XingBie = models.CharField(max_length=200,default='',verbose_name=u'性别')
    NianLing = models.CharField(max_length=200,default='',verbose_name=u'年龄')
    JiGuan = models.CharField(max_length=200,default='',verbose_name=u'籍贯')
    MinZu = models.CharField(max_length=200,default='',verbose_name=u'民族')
    TouXiang = models.CharField(max_length=200,default='',verbose_name=u'头像')
    createtime = models.DateTimeField("创建时间",auto_now_add=True)#自动添加时间
    class Meta:
        verbose_name_plural = '用户列表'
    def __str__(self):
        return self.ZhangHao

class DianPu(models.Model):
    DianPuMing = models.CharField(max_length=200,default='',verbose_name=u'店铺名')
    JianJie = models.CharField(max_length=200,default='',verbose_name=u'简介')
    leixing = models.CharField(max_length=200,default='',verbose_name=u'类型')
    YongYouZhe = models.CharField(max_length=200,default='',verbose_name=u'拥有者')
    ZhaoPai = models.CharField(max_length=200,default='',verbose_name=u'招牌')
    ZhuangTai = models.CharField(max_length=200,default='禁用',verbose_name=u'状态')
    ShiFuTongGuo = models.CharField(max_length=200,default='否',verbose_name=u'是否通过')
    createtime = models.DateTimeField("创建时间",auto_now_add=True)#自动添加时间
    class Meta:
        verbose_name_plural = '商家列表'
    def __str__(self):
        return self.DianPuMing

class LunBoTu(models.Model):
    TuPian = models.CharField(max_length=200,default='',verbose_name=u'图片')
    LianJie = models.CharField(max_length=200,default='',verbose_name=u'简介')
    JianJie = models.CharField(max_length=200,default='',verbose_name=u'链接')
    createtime = models.DateTimeField("创建时间",auto_now_add=True)#自动添加时间
    class Meta:
        verbose_name_plural = '轮播图列表'
    def __str__(self):
        return self.TuPian

class ShangPin(models.Model):
    ShangPinMing = models.CharField(max_length=200,default='',verbose_name=u'商品名')
    JiaGe = models.CharField(max_length=200,default='',verbose_name=u'价格')
    JianJie = models.CharField(max_length=200,default='',verbose_name=u'简介')
    TuPian = models.CharField(max_length=200,default='',verbose_name=u'图片')
    LeiXing = models.CharField(max_length=200,default='',verbose_name=u'类型')
    ShuLiang = models.CharField(max_length=200,default='',verbose_name=u'数量')
    SuoShuShangDian = models.CharField(max_length=200,default='',verbose_name=u'所属商店')
    createtime = models.DateTimeField("创建时间",auto_now_add=True)#自动添加时间
    class Meta:
        verbose_name_plural = '商品列表'
    def __str__(self):
        return self.ShangPinMing

#商品名、价格、简介、图片、类型、数量、所属商店、购买人、购买数量

class GouWuChe(models.Model):
    ShangPinMing = models.CharField(max_length=200,default='',verbose_name=u'商品名')
    JiaGe = models.CharField(max_length=200,default='',verbose_name=u'价格')
    JianJie = models.CharField(max_length=200,default='',verbose_name=u'简介')
    TuPian = models.CharField(max_length=200,default='',verbose_name=u'图片')
    LeiXing = models.CharField(max_length=200,default='',verbose_name=u'类型')
    ShuLiang = models.CharField(max_length=200,default='',verbose_name=u'数量')
    SuoShuShangDian = models.CharField(max_length=200,default='',verbose_name=u'所属商店')
    GouMaiRen = models.CharField(max_length=200,default='',verbose_name=u'购买人')
    GouMaiShuLiang = models.CharField(max_length=200,default='',verbose_name=u'购买数量')
    createtime = models.DateTimeField("创建时间",auto_now_add=True)#自动添加时间
    class Meta:
        verbose_name_plural = '购物车列表'
    def __str__(self):
        return self.ShangPinMing
#省、市、区、街道、电话、姓名、邮编、所属用户

class ShouHuoDiZhi(models.Model):
    Sheng = models.CharField(max_length=200,default='',verbose_name=u'省')
    Shi = models.CharField(max_length=200,default='',verbose_name=u'市')
    Qu = models.CharField(max_length=200,default='',verbose_name=u'区')
    JieDao = models.CharField(max_length=200,default='',verbose_name=u'街道')
    DianHua = models.CharField(max_length=200,default='',verbose_name=u'电话')
    XingMing = models.CharField(max_length=200,default='',verbose_name=u'姓名')
    YouBian = models.CharField(max_length=200,default='',verbose_name=u'邮编')
    SuoShuYongHu = models.CharField(max_length=200,default='',verbose_name=u'所属用户')
    createtime = models.DateTimeField("创建时间",auto_now_add=True)#自动添加时间
    class Meta:
        verbose_name_plural = '收货地址列表'
    def __str__(self):
        return self.Sheng

#省、市、区、街道、电话、姓名、邮编、商品名、价格、简介、图片、类型、数量、所属商店、购买人、购买数量、状态

class DingDan(models.Model):
    Sheng = models.CharField(max_length=200,default='',verbose_name=u'省')
    Shi = models.CharField(max_length=200,default='',verbose_name=u'市')
    Qu = models.CharField(max_length=200,default='',verbose_name=u'区')
    JieDao = models.CharField(max_length=200,default='',verbose_name=u'街道')
    DianHua = models.CharField(max_length=200,default='',verbose_name=u'电话')
    XingMing = models.CharField(max_length=200,default='',verbose_name=u'姓名')
    YouBian = models.CharField(max_length=200,default='',verbose_name=u'邮编')
    ShangPinMing = models.CharField(max_length=200,default='',verbose_name=u'商品名')
    JiaGe = models.CharField(max_length=200,default='',verbose_name=u'价格')
    JianJie = models.CharField(max_length=200,default='',verbose_name=u'简介')
    TuPian = models.CharField(max_length=200,default='',verbose_name=u'图片')
    LeiXing = models.CharField(max_length=200,default='',verbose_name=u'类型')
    ShuLiang = models.CharField(max_length=200,default='',verbose_name=u'数量')
    SuoShuShangDian = models.CharField(max_length=200,default='',verbose_name=u'所属商店')
    GouMaiRen = models.CharField(max_length=200,default='',verbose_name=u'购买人')
    GouMaiShuLiang = models.CharField(max_length=200,default='',verbose_name=u'购买数量')
    ZhuangTai = models.CharField(max_length=200,default='下单',verbose_name=u'状态')
    createtime = models.DateTimeField("创建时间",auto_now_add=True)#自动添加时间
    class Meta:
        verbose_name_plural = '订单列表'
    def __str__(self):
        return self.Sheng

#评价人、评价时间、评价内容、评价商品

class PingJia(models.Model):
    PingJiaRen = models.CharField(max_length=200,default='',verbose_name=u'评价人')
    PingJiaShiJian = models.CharField(max_length=200,default='',verbose_name=u'评价时间')
    PingJiaNaRong = models.CharField(max_length=200,default='',verbose_name=u'评价内容')
    PingJiaShangPin = models.CharField(max_length=200,default='',verbose_name=u'评价商品')
    createtime = models.DateTimeField("创建时间",auto_now_add=True)#自动添加时间
    class Meta:
        verbose_name_plural = '评价列表'
    def __str__(self):
        return self.PingJiaRen

#称呼、邮箱、标题、信息

class ZaiXianLiuYan(models.Model):
    ChenHu = models.CharField(max_length=200,default='',verbose_name=u'称呼')
    YouXiang = models.CharField(max_length=200,default='',verbose_name=u'邮箱')
    BiaoTi = models.CharField(max_length=200,default='',verbose_name=u'标题')
    XinXi = models.CharField(max_length=200,default='',verbose_name=u'信息')
    createtime = models.DateTimeField("创建时间",auto_now_add=True)#自动添加时间
    class Meta:
        verbose_name_plural = '在线留言列表'
    def __str__(self):
        return self.ChenHu

#商品名、价格、简介、图片、类型、数量、所属商店、浏览人、浏览时间

class LiuLan(models.Model):
    ShangPinMing = models.CharField(max_length=200,default='',verbose_name=u'商品名')
    JiaGe = models.CharField(max_length=200,default='',verbose_name=u'价格')
    JianJie = models.CharField(max_length=200,default='',verbose_name=u'简介')
    TuPian = models.CharField(max_length=200,default='',verbose_name=u'图片')
    LeiXing = models.CharField(max_length=200,default='',verbose_name=u'类型')
    ShuLiang = models.CharField(max_length=200,default='',verbose_name=u'数量')
    SuoShuShangDian = models.CharField(max_length=200,default='',verbose_name=u'所属商店')
    LiuLanRen = models.CharField(max_length=200,default='',verbose_name=u'浏览人')
    LiuLanShiJian = models.CharField(max_length=200,default='',verbose_name=u'浏览时间')
    wid = models.CharField(max_length=200,default='',verbose_name=u'物品id')
    createtime = models.DateTimeField("创建时间",auto_now_add=True)#自动添加时间
    class Meta:
        verbose_name_plural = '浏览列表'
    def __str__(self):
        return self.ShangPinMing


