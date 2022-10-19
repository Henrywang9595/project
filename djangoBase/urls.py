"""djangoBase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from . import view,testdb
from django.conf.urls.static import static
from django.conf import settings

from django.shortcuts import render, render_to_response

from djangoBaseModel.models import YongHu
from djangoBaseModel.models import DianPu
from djangoBaseModel.models import LunBoTu
from djangoBaseModel.models import DianPu
from djangoBaseModel.models import ShangPin
from djangoBaseModel.models import KeHu
from djangoBaseModel.models import GouWuChe
from djangoBaseModel.models import ShouHuoDiZhi
from djangoBaseModel.models import DingDan
from djangoBaseModel.models import PingJia

from django.http import HttpResponse
from django.shortcuts import render
from django.forms.models import model_to_dict
import json

from django.http import JsonResponse
import os
import time


from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random
 
def getRandomColor():
    '''获取一个随机颜色(r,g,b)格式的'''
    c1 = random.randint(0,255)
    c2 = random.randint(0,255)
    c3 = random.randint(0,255)
    return (c1,c2,c3)
 
 
def getRandomStr():
    '''获取一个随机字符串，每个字符的颜色也是随机的'''
    random_num = str(random.randint(0, 9))
    random_low_alpha = chr(random.randint(97, 122))
    random_upper_alpha = chr(random.randint(65, 90))
    random_char = random.choice([random_num, random_low_alpha, random_upper_alpha])
 
    return random_char

def duanXinCode(request):
    string = ''
    for i in range(5):
        # 循环5次，获取5个随机字符串
        random_char = getRandomStr()
        string=string+random_char
    return JsonResponse({"code":string,"phone":request.POST['phone']},content_type="application/json")


def getYanZhengMa(request):

     
    # 获取一个Image对象，参数分别是RGB模式。宽150，高30，随机颜色
    image = Image.new('RGB',(150,50),getRandomColor())
     
    # 获取一个画笔对象，将图片对象传过去
    draw = ImageDraw.Draw(image)
     
    # 获取一个font字体对象参数是ttf的字体文件的目录，以及字体的大小
    font=ImageFont.truetype("kumo.ttf",size=26)
     
    string = ''
    for i in range(5):
        # 循环5次，获取5个随机字符串
        random_char = getRandomStr()
     
        # 在图片上一次写入得到的随机字符串,参数是：定位，字符串，颜色，字体
        draw.text((10+i*30, 0),random_char , getRandomColor(), font=font)
        string=string+random_char
     
    # 噪点噪线
    width=150
    height=50
    # 划线
    for i in range(5):
        x1=random.randint(0,width)
        x2=random.randint(0,width)
        y1=random.randint(0,height)
        y2=random.randint(0,height)
        draw.line((x1,y1,x2,y2),fill=getRandomColor())
     
    # 画点
    for i in range(30):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=getRandomColor())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=getRandomColor())
    imgName = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))+'.png'
    image.save(open(imgName, 'wb'), 'png')
    os.system('mv '+imgName+' static/'+imgName)
    return JsonResponse({"msg":string,'path':imgName},content_type="application/json")
def getallxin(request):
    response3 = zhanneixin.objects.all()
    if response3:
        context          = []
        for x in response3:
            context.append(model_to_dict(x))
            pass
        return JsonResponse({"msg":'','data':context},content_type="application/json")
    return JsonResponse({"msg":'no data','data':[]})

def selectAllDianPu(request):
    response3 = DianPu.objects.all()
    if response3:
        context = []
        for x in response3:
            try:
                qq = request.GET['q']
                d = model_to_dict(x)
                if d['YongYouZhe']!=qq:
                    continue
                    pass
                pass
            except Exception as e:
                print(e)
            context.append(model_to_dict(x))
            pass
        return JsonResponse({"msg":"",'data':context},content_type="application/json")
    return JsonResponse({"msg":"没有数据",'data':[]},content_type="application/json")
def getallresult(request):
    # os.system('cd static/main/data && python -m SimpleHTTPServer 8080')
    filePath = 'static/main/'
    alsit = os.listdir(filePath)
    tlist = []
    for x in alsit:
        if 'html' in x:
            tlist.append(x)
            pass
        pass
    print(alsit)
    return JsonResponse({"msg":'成功','data':tlist},content_type="application/json")

def zhuce(request):
    user1 = YongHu()
    try:
        if request.POST:
            user1.ZhangHao = str(request.POST['name'])
            user1.MiMa = str(request.POST['pwd'])
        user1.save()
        pass
    except Exception as e:
        return JsonResponse({"msg":'注册失败，账号已存在'},content_type="application/json")
        raise
    return JsonResponse({"msg":'注册成功'},content_type="application/json")
def denglu2(request):
    if request.POST:
        try:
            response3 = KeHu.objects.filter(ZhangHao=request.POST['name']) 
            if response3:
                context          = {}
                for x in response3:
                    context = model_to_dict(x)
                    print(context)
                    if request.POST['pwd']==context['MiMa']:
                        return JsonResponse({"msg":'登录成功'},content_type="application/json")
                        pass
                    return JsonResponse({"msg":'账号或密码错误！3'},content_type="application/json")
                    pass
        except Exception as e:
            return JsonResponse({"msg":'账号或密码错误！','e':str(e)},content_type="application/json")
    return JsonResponse({"msg":'账号或密码错误！1'},content_type="application/json")


def denglu(request):
    if request.POST:
        try:
            response3 = YongHu.objects.get(ZhangHao=request.POST['name']) 
            if response3:
                context          = {}
                context = model_to_dict(response3)
                if request.POST['pwd']==context['MiMa']:
                    return JsonResponse({"msg":'登录成功'},content_type="application/json")
                    pass
                return JsonResponse({"msg":'账号或密码错误！'},content_type="application/json")
        except Exception as e:
            return JsonResponse({"msg":'账号或密码错误！'},content_type="application/json")
    return JsonResponse({"msg":'账号或密码错误！'},content_type="application/json")

from django.http import JsonResponse
def getuserinfor(request):
    response3 = YongHu.objects.get(ZhangHao=request.POST['name']) 
    if response3:
        context          = {}
        context = model_to_dict(response3)
        return JsonResponse({"msg":'','data':context},content_type="application/json")
    return JsonResponse({"msg":'no data'})

def getdata(request):
    import air_BSGS_2018
    citys = request.POST['city']
    nianfen = request.POST['nianfen']
    dingshi = request.POST['dingshi']
    if dingshi==0:
        air_BSGS_2018.getdata(citys.split(','),nianfen)
        pass
    else:
        while 1:
            air_BSGS_2018.getdata(citys.split(','),nianfen)
            time.sleep(int(dingshi)*3600)
            pass
    return JsonResponse({"msg":'爬取成功'})

    pass
import uuid,hashlib

def get_unique_str():
    uuid_str = str(uuid.uuid4())
    md5 = hashlib.md5()
    md5.update(uuid_str.encode('utf-8'))
    return md5.hexdigest()

def daoruaction(req):
    file_obj = req.FILES.get('icon')
    f = open('air_beijing_2018.csv','wb')
    path = 'static/upload/'+ get_unique_str() + file_obj.name
    with open(path, 'wb') as f:
        for i in file_obj.chunks():
            f.write(i)
    f.close()
    return JsonResponse({"msg":'上传成功','path':path})


# 新增用户

def addYongHu(request):
    data = YongHu()
    if request.POST:
        data.ZhangHao=str(request.POST['ZhangHao'])
        data.MiMa=str(request.POST['MiMa'])
        data.XingMing=str(request.POST['XingMing'])
        data.XingBie=str(request.POST['XingBie'])
        data.NianLing=str(request.POST['NianLing'])
        data.JiGuan=str(request.POST['JiGuan'])
        data.MinZu=str(request.POST['MinZu'])
        data.TouXiang=str(request.POST['TouXiang'])
    data.save()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")

# 修改用户

def updateYongHu(request):
    data = YongHu.objects.get(id=request.POST['id'])
    if request.POST:
        data.ZhangHao=str(request.POST['ZhangHao'])
        data.MiMa=str(request.POST['MiMa'])
        data.XingMing=str(request.POST['XingMing'])
        data.XingBie=str(request.POST['XingBie'])
        data.NianLing=str(request.POST['NianLing'])
        data.JiGuan=str(request.POST['JiGuan'])
        data.MinZu=str(request.POST['MinZu'])
        data.TouXiang=str(request.POST['TouXiang'])
    data.save()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")

# 删除用户
def selectAllYongHu(request):
    response3 = KeHu.objects.all()
    if response3:
        context = []
        for x in response3:
            context.append(model_to_dict(x))
            pass
        return JsonResponse({"msg":"操作成功",'data':context},content_type="application/json")
    return JsonResponse({"msg":"没有数据","data":[]},content_type="application/json")

def deleteYongHu(request):
    data = YongHu.objects.get(id=request.POST['id'])
    data.delete()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")

# 新增店铺

def addDianPu(request):
    data = DianPu()
    if request.POST:
        data.DianPuMing=str(request.POST['DianPuMing'])
        data.JianJie=str(request.POST['JianJie'])
        data.YongYouZhe=str(request.POST['YongYouZhe'])
        data.ZhaoPai=str(request.POST['ZhaoPai'])
        # data.ZhuangTai=str(request.POST['ZhuangTai'])
        # data.ShiFuTongGuo=str(request.POST['ShiFuTongGuo'])
    data.save()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")

# 修改店铺

def updateDianPu(request):
    data = DianPu.objects.get(id=request.POST['id'])
    if request.POST:
        data.DianPuMing=str(request.POST['DianPuMing'])
        data.JianJie=str(request.POST['JianJie'])
        data.YongYouZhe=str(request.POST['YongYouZhe'])
        data.ZhaoPai=str(request.POST['ZhaoPai'])
        data.ZhuangTai=str(request.POST['ZhuangTai'])
        data.ShiFuTongGuo=str(request.POST['ShiFuTongGuo'])
    data.save()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")

# 删除店铺

def deleteDianPu(request):
    data = DianPu.objects.get(id=request.POST['id'])
    data.delete()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")

# 新增轮播图

def addLunBoTu(request):
    data = LunBoTu()
    if request.POST:
        data.TuPian=str(request.POST['TuPian'])
        data.LianJie=str(request.POST['LianJie'])
    data.save()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")

# 修改轮播图

def updateLunBoTu(request):
    data = LunBoTu.objects.get(id=request.POST['id'])
    if request.POST:
        data.TuPian=str(request.POST['TuPian'])
        data.LianJie=str(request.POST['LianJie'])
    data.save()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")

# 删除轮播图

def deleteLunBoTu(request):
    data = LunBoTu.objects.get(id=request.POST['id'])
    data.delete()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")
def selectAlllunbotu(request):
    response3 = LunBoTu.objects.all()
    if response3:
        context = []
        for x in response3:
            context.append(model_to_dict(x))
            pass
        return JsonResponse({"msg":"",'data':context},content_type="application/json")
    return JsonResponse({"msg":"没有数据",'data':[]},content_type="application/json")

# 新增商品

def addShangPin(request):
    data = ShangPin()
    if request.POST:
        data.ShangPinMing=str(request.POST['ShangPinMing'])
        data.JiaGe=str(request.POST['JiaGe'])
        data.JianJie=str(request.POST['JianJie'])
        data.TuPian=str(request.POST['TuPian'])
        data.LeiXing=str(request.POST['LeiXing'])
        data.ShuLiang=str(request.POST['ShuLiang'])
        data.SuoShuShangDian=str(request.POST['SuoShuShangDian'])

    data.save()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")

# 修改商品

def updateShangPin(request):
    data = ShangPin.objects.get(id=request.POST['id'])
    if request.POST:
        data.ShangPinMing=str(request.POST['ShangPinMing'])
        data.JiaGe=str(request.POST['JiaGe'])
        data.JianJie=str(request.POST['JianJie'])
        data.TuPian=str(request.POST['TuPian'])
        data.LeiXing=str(request.POST['LeiXing'])
        data.ShuLiang=str(request.POST['ShuLiang'])
        data.SuoShuShangDian=str(request.POST['SuoShuShangDian'])

    data.save()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")

# 删除商品

def deleteShangPin(request):
    data = ShangPin.objects.get(id=request.POST['id'])
    data.delete()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")


# 查询所有商品

def selectAllShangPin(request):
    response3 = ShangPin.objects.all()
    if response3:
        context = []
        for x in response3:
            context.append(model_to_dict(x))
            pass
        return JsonResponse({"msg":"操作成功",'data':context},content_type="application/json")
    return JsonResponse({"msg":"没有数据",'data':[]},content_type="application/json")
# 新增客户


def addKeHu(request):
    data = KeHu()
    if request.POST:
        try:
            data.ZhangHao=str(request.POST['ZhangHao'])
        except Exception as e:
            print("账号字段没更改")
        try:
            data.MiMa=str(request.POST['MiMa'])
        except Exception as e:
            print("密码字段没更改")
        try:
            data.YongHuMing=str(request.POST['YongHuMing'])
        except Exception as e:
            print("用户名字段没更改")
        try:
            data.XingBie=str(request.POST['XingBie'])
        except Exception as e:
            print("性别字段没更改")
        try:
            data.NianLing=str(request.POST['NianLing'])
        except Exception as e:
            print("年龄字段没更改")
        try:
            data.TouXiang=str(request.POST['TouXiang'])
        except Exception as e:
            print("头像字段没更改")
    data.save()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")

# 修改客户

def updateKeHu(request):
    data = KeHu.objects.get(id=request.POST['id'])
    if request.POST:
        data.ZhangHao=str(request.POST['ZhangHao'])
        data.MiMa=str(request.POST['MiMa'])
        data.YongHuMing=str(request.POST['YongHuMing'])
        data.XingBie=str(request.POST['XingBie'])
        data.NianLing=str(request.POST['NianLing'])
        data.TouXiang=str(request.POST['TouXiang'])
    data.save()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")

# 删除客户

def deleteKeHu(request):
    data = KeHu.objects.get(id=request.POST['id'])
    data.delete()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")


# 查询所有客户

def selectAllKeHu(request):
    response3 = KeHu.objects.all()
    if response3:
        context = []
        for x in response3:
            context.append(model_to_dict(x))
            pass
        return JsonResponse({"msg":"操作成功",'data':context},content_type="application/json")
    return JsonResponse({"msg":"没有数据","data":[]},content_type="application/json")
# 新增购物车

def addGouWuChe(request):
    data = GouWuChe()
    if request.POST:
        data.ShangPinMing=str(request.POST['ShangPinMing'])
        data.JiaGe=str(request.POST['JiaGe'])
        data.JianJie=str(request.POST['JianJie'])
        data.TuPian=str(request.POST['TuPian'])
        data.LeiXing=str(request.POST['LeiXing'])
        data.ShuLiang=str(request.POST['ShuLiang'])
        data.SuoShuShangDian=str(request.POST['SuoShuShangDian'])
        data.GouMaiRen=str(request.POST['GouMaiRen'])
        data.GouMaiShuLiang=str(request.POST['GouMaiShuLiang'])
    data.save()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")

# 修改购物车

def updateGouWuChe(request):
    data = GouWuChe.objects.get(id=request.POST['id'])
    if request.POST:
        data.ShangPinMing=str(request.POST['ShangPinMing'])
        data.JiaGe=str(request.POST['JiaGe'])
        data.JianJie=str(request.POST['JianJie'])
        data.TuPian=str(request.POST['TuPian'])
        data.LeiXing=str(request.POST['LeiXing'])
        data.ShuLiang=str(request.POST['ShuLiang'])
        data.SuoShuShangDian=str(request.POST['SuoShuShangDian'])
        data.GouMaiRen=str(request.POST['GouMaiRen'])
        data.GouMaiShuLiang=str(request.POST['GouMaiShuLiang'])
    data.save()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")

# 删除购物车

def deleteGouWuChe(request):
    data = GouWuChe.objects.get(id=request.POST['id'])
    data.delete()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")


# 查询所有购物车

def selectAllGouWuChe(request):
    response3 = GouWuChe.objects.all()
    try:
        if request.POST['GouMaiRen']:
            response3 = GouWuChe.objects.filter(GouMaiRen=request.POST['GouMaiRen'])
            pass
        pass
    except Exception as e:
        print('')
    if response3:
        context = []
        for x in response3:
            context.append(model_to_dict(x))
            pass
        return JsonResponse({"msg":"操作成功",'data':context},content_type="application/json")
    return JsonResponse({"msg":"没有数据","data":[]},content_type="application/json")
# 新增收货地址

def addShouHuoDiZhi(request):
    data = ShouHuoDiZhi()
    if request.POST:
        data.Sheng=str(request.POST['Sheng'])
        data.Shi=str(request.POST['Shi'])
        data.Qu=str(request.POST['Qu'])
        data.JieDao=str(request.POST['JieDao'])
        data.DianHua=str(request.POST['DianHua'])
        data.XingMing=str(request.POST['XingMing'])
        data.YouBian=str(request.POST['YouBian'])
        data.SuoShuYongHu=str(request.POST['SuoShuYongHu'])
    data.save()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")

# 修改收货地址

def updateShouHuoDiZhi(request):
    data = ShouHuoDiZhi.objects.get(id=request.POST['id'])
    if request.POST:
        data.Sheng=str(request.POST['Sheng'])
        data.Shi=str(request.POST['Shi'])
        data.Qu=str(request.POST['Qu'])
        data.JieDao=str(request.POST['JieDao'])
        data.DianHua=str(request.POST['DianHua'])
        data.XingMing=str(request.POST['XingMing'])
        data.YouBian=str(request.POST['YouBian'])
        data.SuoShuYongHu=str(request.POST['SuoShuYongHu'])
    data.save()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")

# 删除收货地址

def deleteShouHuoDiZhi(request):
    data = ShouHuoDiZhi.objects.get(id=request.POST['id'])
    data.delete()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")


# 查询所有收货地址

def selectAllShouHuoDiZhi(request):
    response3 = ShouHuoDiZhi.objects.all()
    if request.POST['GouMaiRen']:
        response3 = ShouHuoDiZhi.objects.filter(SuoShuYongHu=request.POST['GouMaiRen'])
        pass
    if response3:
        context = []
        for x in response3:
            context.append(model_to_dict(x))
            pass
        return JsonResponse({"msg":"操作成功",'data':context},content_type="application/json")
    return JsonResponse({"msg":"没有数据","data":[]},content_type="application/json")
# 新增订单

def addDingDan(request):
    data = DingDan()
    if request.POST:
        data.Sheng=str(request.POST['Sheng'])
        data.Shi=str(request.POST['Shi'])
        data.Qu=str(request.POST['Qu'])
        data.JieDao=str(request.POST['JieDao'])
        data.DianHua=str(request.POST['DianHua'])
        data.XingMing=str(request.POST['XingMing'])
        data.YouBian=str(request.POST['YouBian'])
        data.ShangPinMing=str(request.POST['ShangPinMing'])
        data.JiaGe=str(request.POST['JiaGe'])
        data.JianJie=str(request.POST['JianJie'])
        data.TuPian=str(request.POST['TuPian'])
        data.LeiXing=str(request.POST['LeiXing'])
        data.ShuLiang=str(request.POST['ShuLiang'])
        data.SuoShuShangDian=str(request.POST['SuoShuShangDian'])
        data.GouMaiRen=str(request.POST['GouMaiRen'])
        data.GouMaiShuLiang=str(request.POST['GouMaiShuLiang'])
        data.ZhuangTai=str(request.POST['ZhuangTai'])
    data.save()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")

# 修改订单

def updateDingDan(request):
    data = DingDan.objects.get(id=request.POST['id'])
    if request.POST:
        data.Sheng=str(request.POST['Sheng'])
        data.Shi=str(request.POST['Shi'])
        data.Qu=str(request.POST['Qu'])
        data.JieDao=str(request.POST['JieDao'])
        data.DianHua=str(request.POST['DianHua'])
        data.XingMing=str(request.POST['XingMing'])
        data.YouBian=str(request.POST['YouBian'])
        data.ShangPinMing=str(request.POST['ShangPinMing'])
        data.JiaGe=str(request.POST['JiaGe'])
        data.JianJie=str(request.POST['JianJie'])
        data.TuPian=str(request.POST['TuPian'])
        data.LeiXing=str(request.POST['LeiXing'])
        data.ShuLiang=str(request.POST['ShuLiang'])
        data.SuoShuShangDian=str(request.POST['SuoShuShangDian'])
        data.GouMaiRen=str(request.POST['GouMaiRen'])
        data.GouMaiShuLiang=str(request.POST['GouMaiShuLiang'])
        data.ZhuangTai=str(request.POST['ZhuangTai'])
    data.save()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")

# 删除订单

def deleteDingDan(request):
    data = DingDan.objects.get(id=request.POST['id'])
    data.delete()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")


# 查询所有订单

def selectAllDingDan(request):
    response3 = DingDan.objects.all()
    try:
        if request.POST['GouMaiRen']:
            response3 = DingDan.objects.filter(GouMaiRen=request.POST['GouMaiRen'])
            pass
        pass
    except Exception as e:
        print("")


    if response3:
        context = []
        for x in response3:
            context.append(model_to_dict(x))
            pass
        return JsonResponse({"msg":"操作成功",'data':context},content_type="application/json")
    return JsonResponse({"msg":"没有数据","data":[]},content_type="application/json")
# 新增评价

def addPingJia(request):
    data = PingJia()
    if request.POST:
        data.PingJiaRen=str(request.POST['PingJiaRen'])
        data.PingJiaShiJian=str(request.POST['PingJiaShiJian'])
        data.PingJiaNaRong=str(request.POST['PingJiaNaRong'])
        data.PingJiaShangPin=str(request.POST['PingJiaShangPin'])
    data.save()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")

# 修改评价

def updatePingJia(request):
    data = PingJia.objects.get(id=request.POST['id'])
    if request.POST:
        data.PingJiaRen=str(request.POST['PingJiaRen'])
        data.PingJiaShiJian=str(request.POST['PingJiaShiJian'])
        data.PingJiaNaRong=str(request.POST['PingJiaNaRong'])
        data.PingJiaShangPin=str(request.POST['PingJiaShangPin'])
    data.save()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")

# 删除评价

def deletePingJia(request):
    data = PingJia.objects.get(id=request.POST['id'])
    data.delete()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")


# 查询所有评价

def selectAllPingJia(request):
    response3 = PingJia.objects.all()
    if response3:
        context = []
        for x in response3:
            context.append(model_to_dict(x))
            pass
        return JsonResponse({"msg":"操作成功",'data':context},content_type="application/json")
    return JsonResponse({"msg":"没有数据","data":[]},content_type="application/json")


from djangoBaseModel.models import ZaiXianLiuYan

# 新增在线留言

def addZaiXianLiuYan(request):
    data = ZaiXianLiuYan()
    if request.POST:
        try:
            data.ChenHu=str(request.POST['ChenHu'])
        except Exception as e:
            print("称呼字段没更改")
        try:
            data.YouXiang=str(request.POST['YouXiang'])
        except Exception as e:
            print("邮箱字段没更改")
        try:
            data.BiaoTi=str(request.POST['BiaoTi'])
        except Exception as e:
            print("标题字段没更改")
        try:
            data.XinXi=str(request.POST['XinXi'])
        except Exception as e:
            print("信息字段没更改")
    data.save()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")

# 修改在线留言

def updateZaiXianLiuYan(request):
    data = ZaiXianLiuYan.objects.get(id=request.POST['id'])
    if request.POST:
        try:
            data.ChenHu=str(request.POST['ChenHu'])
        except Exception as e:
            print("称呼字段没更改")
        try:
            data.YouXiang=str(request.POST['YouXiang'])
        except Exception as e:
            print("邮箱字段没更改")
        try:
            data.BiaoTi=str(request.POST['BiaoTi'])
        except Exception as e:
            print("标题字段没更改")
        try:
            data.XinXi=str(request.POST['XinXi'])
        except Exception as e:
            print("信息字段没更改")
    data.save()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")

# 删除在线留言

def deleteZaiXianLiuYan(request):
    data = ZaiXianLiuYan.objects.get(id=request.POST['id'])
    data.delete()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")


# 查询所有在线留言

def selectAllZaiXianLiuYan(request):
    response3 = ZaiXianLiuYan.objects.all()
    if response3:
        context = []
        for x in response3:
            context.append(model_to_dict(x))
            pass
        return JsonResponse({"msg":"操作成功",'data':context},content_type="application/json")
    return JsonResponse({"msg":"没有数据","data":[]},content_type="application/json")


# 根据条件查询在线留言

def selectZaiXianLiuYanbykey(request):
    from django.db.models import Q
    q1 = Q()
    q1.connector = 'OR'
    try:
        if request.POST['ChenHu']!='':
            q1.children.append(('ChenHu__icontains', request.POST['ChenHu']))
            pass
        pass
    except Exception as e:
        print("没传这个参数")
    try:
        if request.POST['YouXiang']!='':
            q1.children.append(('YouXiang__icontains', request.POST['YouXiang']))
            pass
        pass
    except Exception as e:
        print("没传这个参数")
    try:
        if request.POST['BiaoTi']!='':
            q1.children.append(('BiaoTi__icontains', request.POST['BiaoTi']))
            pass
        pass
    except Exception as e:
        print("没传这个参数")
    try:
        if request.POST['XinXi']!='':
            q1.children.append(('XinXi__icontains', request.POST['XinXi']))
            pass
        pass
    except Exception as e:
        print("没传这个参数")
    response3 = ZaiXianLiuYan.objects.filter(q1)
    if response3:
        context = []
        for x in response3:
            context.append(model_to_dict(x))
            pass
        return JsonResponse({"msg":"操作成功","data":context},content_type="application/json")
    return JsonResponse({"msg":"没有数据","data":[]},content_type="application/json")


from djangoBaseModel.models import LiuLan

# 新增浏览

def addLiuLan(request):
    data = LiuLan()
    if request.POST:
        try:
            data.ShangPinMing=str(request.POST['ShangPinMing'])
        except Exception as e:
            print("商品名字段没更改")
        try:
            data.JiaGe=str(request.POST['JiaGe'])
        except Exception as e:
            print("价格字段没更改")
        try:
            data.JianJie=str(request.POST['JianJie'])
        except Exception as e:
            print("简介字段没更改")
        try:
            data.TuPian=str(request.POST['TuPian'])
        except Exception as e:
            print("图片字段没更改")
        try:
            data.LeiXing=str(request.POST['LeiXing'])
        except Exception as e:
            print("类型字段没更改")
        try:
            data.ShuLiang=str(request.POST['ShuLiang'])
        except Exception as e:
            print("数量字段没更改")
        try:
            data.SuoShuShangDian=str(request.POST['SuoShuShangDian'])
        except Exception as e:
            print("所属商店字段没更改")
        try:
            data.LiuLanRen=str(request.POST['LiuLanRen'])
        except Exception as e:
            print("浏览人字段没更改")
        try:
            data.LiuLanShiJian=str(request.POST['LiuLanShiJian'])
        except Exception as e:
            print("浏览时间字段没更改")

        try:
            data.wid=str(request.POST['wid'])
        except Exception as e:
            print("浏览时间字段没更改")


            
    data.save()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")

# 修改浏览

def updateLiuLan(request):
    data = LiuLan.objects.get(id=request.POST['id'])
    if request.POST:
        try:
            data.ShangPinMing=str(request.POST['ShangPinMing'])
        except Exception as e:
            print("商品名字段没更改")
        try:
            data.JiaGe=str(request.POST['JiaGe'])
        except Exception as e:
            print("价格字段没更改")
        try:
            data.JianJie=str(request.POST['JianJie'])
        except Exception as e:
            print("简介字段没更改")
        try:
            data.TuPian=str(request.POST['TuPian'])
        except Exception as e:
            print("图片字段没更改")
        try:
            data.LeiXing=str(request.POST['LeiXing'])
        except Exception as e:
            print("类型字段没更改")
        try:
            data.ShuLiang=str(request.POST['ShuLiang'])
        except Exception as e:
            print("数量字段没更改")
        try:
            data.SuoShuShangDian=str(request.POST['SuoShuShangDian'])
        except Exception as e:
            print("所属商店字段没更改")
        try:
            data.LiuLanRen=str(request.POST['LiuLanRen'])
        except Exception as e:
            print("浏览人字段没更改")
        try:
            data.LiuLanShiJian=str(request.POST['LiuLanShiJian'])
        except Exception as e:
            print("浏览时间字段没更改")
    data.save()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")

# 删除浏览

def deleteLiuLan(request):
    data = LiuLan.objects.get(id=request.POST['id'])
    data.delete()
    return JsonResponse({"msg":"操作成功"},content_type="application/json")


# 查询所有浏览

def selectAllLiuLan(request):
    response3 = LiuLan.objects.all()
    if response3:
        context = []
        for x in response3:
            context.append(model_to_dict(x))
            pass
        return JsonResponse({"msg":"操作成功",'data':context},content_type="application/json")
    return JsonResponse({"msg":"没有数据","data":[]},content_type="application/json")


# 根据条件查询浏览

def selectLiuLanbykey(request):
    from django.db.models import Q
    q1 = Q()
    q1.connector = 'OR'
    try:
        if request.POST['ShangPinMing']!='':
            q1.children.append(('ShangPinMing__icontains', request.POST['ShangPinMing']))
            pass
        pass
    except Exception as e:
        print("没传这个参数")
    try:
        if request.POST['JiaGe']!='':
            q1.children.append(('JiaGe__icontains', request.POST['JiaGe']))
            pass
        pass
    except Exception as e:
        print("没传这个参数")
    try:
        if request.POST['JianJie']!='':
            q1.children.append(('JianJie__icontains', request.POST['JianJie']))
            pass
        pass
    except Exception as e:
        print("没传这个参数")
    try:
        if request.POST['TuPian']!='':
            q1.children.append(('TuPian__icontains', request.POST['TuPian']))
            pass
        pass
    except Exception as e:
        print("没传这个参数")
    try:
        if request.POST['LeiXing']!='':
            q1.children.append(('LeiXing__icontains', request.POST['LeiXing']))
            pass
        pass
    except Exception as e:
        print("没传这个参数")
    try:
        if request.POST['ShuLiang']!='':
            q1.children.append(('ShuLiang__icontains', request.POST['ShuLiang']))
            pass
        pass
    except Exception as e:
        print("没传这个参数")
    try:
        if request.POST['SuoShuShangDian']!='':
            q1.children.append(('SuoShuShangDian__icontains', request.POST['SuoShuShangDian']))
            pass
        pass
    except Exception as e:
        print("没传这个参数")
    try:
        if request.POST['LiuLanRen']!='':
            q1.children.append(('LiuLanRen__icontains', request.POST['LiuLanRen']))
            pass
        pass
    except Exception as e:
        print("没传这个参数")
    try:
        if request.POST['LiuLanShiJian']!='':
            q1.children.append(('LiuLanShiJian__icontains', request.POST['LiuLanShiJian']))
            pass
        pass
    except Exception as e:
        print("没传这个参数")
    response3 = LiuLan.objects.filter(q1)
    if response3:
        context = []
        for x in response3:
            context.append(model_to_dict(x))
            pass
        return JsonResponse({"msg":"操作成功","data":context},content_type="application/json")
    return JsonResponse({"msg":"没有数据","data":[]},content_type="application/json")




urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', view.shouye),
    url(r'^regist\.html$', view.regist),
    url(r'^shouye\.html$', view.shouye),
    url(r'^index\.html$', view.yonghudenglu),
    url(r'^shangpingsousuojieguo\.html$', view.shangpingsousuojieguo),

    url(r'^main\.html$', view.main),
    url(r'^daoru\.html$', view.daoru),
    url(r'^dianpulist\.html$', view.dianpulist),
    url(r'^shangpinglist\.html$', view.shangpinglist),
    url(r'^shangpingliebiao\.html$', view.shangpingliebiao),
    url(r'^shangpingxiangqing\.html$', view.shangpingxiangqing),
    url(r'^wodedingdan\.html$', view.wodedingdan),
    url(r'^gouwuche\.html$', view.gouwuche),
    url(r'^shouhuodizhi\.html$', view.ShouHuoDiZhi),
    url(r'^dingdanliebiaohoutai\.html$', view.dingdanliebiaohoutai),
    url(r'^qian\.html$', view.yonghudenglu),
    url(r'^hou\.html$', view.hou),
    url(r'^userCenter\.html$', view.userCenter),
    url(r'^about\.html$', view.about),
    url(r'^contact\.html$', view.contact),
    url(r'^zaixianliuyan\.html$', view.zaixianliuyan),

# 在线留言路由

    url(r'^addZaiXianLiuYan$', addZaiXianLiuYan),
    url(r'^updateZaiXianLiuYan$', updateZaiXianLiuYan),
    url(r'^deleteZaiXianLiuYan$', deleteZaiXianLiuYan),
    url(r'^selectAllZaiXianLiuYan$', selectAllZaiXianLiuYan),
    url(r'^selectZaiXianLiuYanbykey$', selectZaiXianLiuYanbykey),


    url(r'^getdata$', getdata),
    url(r'^savedata$', testdb.savedata),
    url(r'^getuserinfor$', getuserinfor),
    url(r'^getYanZhengMa$', getYanZhengMa),
    url(r'^duanXinCode$', duanXinCode),
    url(r'^daoruaction$', daoruaction),
    url(r'^selectAlllunbotu$', selectAlllunbotu),

    url(r'^zhuce$', zhuce),
    url(r'^denglu$', denglu),
    url(r'^getallresult$', getallresult),
    url(r'^selectAllDianPu$', selectAllDianPu),
    url(r'^denglu2$', denglu2),

# 用户路由

    url(r'^addYongHu$', addYongHu),
    url(r'^updateYongHu$', updateYongHu),
    url(r'^selectAllYongHu$', selectAllYongHu),
    url(r'^deleteYongHu$', deleteYongHu),


# 浏览路由

    url(r'^addLiuLan$', addLiuLan),
    url(r'^updateLiuLan$', updateLiuLan),
    url(r'^deleteLiuLan$', deleteLiuLan),
    url(r'^selectAllLiuLan$', selectAllLiuLan),
    url(r'^selectLiuLanbykey$', selectLiuLanbykey),


# 店铺路由

    url(r'^addDianPu$', addDianPu),
    url(r'^updateDianPu$', updateDianPu),
    url(r'^deleteDianPu$', deleteDianPu),
# 轮播图路由

    url(r'^addLunBoTu$', addLunBoTu),
    url(r'^updateLunBoTu$', updateLunBoTu),
    url(r'^deleteLunBoTu$', deleteLunBoTu),
# 商品路由

    url(r'^addShangPin$', addShangPin),
    url(r'^updateShangPin$', updateShangPin),
    url(r'^deleteShangPin$', deleteShangPin),
    url(r'^selectAllShangPin$', selectAllShangPin),
# 客户路由

    url(r'^addKeHu$', addKeHu),
    url(r'^updateKeHu$', updateKeHu),
    url(r'^deleteKeHu$', deleteKeHu),
    url(r'^selectAllKeHu$', selectAllKeHu),
# 购物车路由

    url(r'^addGouWuChe$', addGouWuChe),
    url(r'^updateGouWuChe$', updateGouWuChe),
    url(r'^deleteGouWuChe$', deleteGouWuChe),
    url(r'^selectAllGouWuChe$', selectAllGouWuChe),
# 收货地址路由

    url(r'^addShouHuoDiZhi$', addShouHuoDiZhi),
    url(r'^updateShouHuoDiZhi$', updateShouHuoDiZhi),
    url(r'^deleteShouHuoDiZhi$', deleteShouHuoDiZhi),
    url(r'^selectAllShouHuoDiZhi$', selectAllShouHuoDiZhi),

    # 订单路由

    url(r'^addDingDan$', addDingDan),
    url(r'^updateDingDan$', updateDingDan),
    url(r'^deleteDingDan$', deleteDingDan),
    url(r'^selectAllDingDan$', selectAllDingDan),

    # 评价路由

    url(r'^addPingJia$', addPingJia),
    url(r'^updatePingJia$', updatePingJia),
    url(r'^deletePingJia$', deletePingJia),
    url(r'^selectAllPingJia$', selectAllPingJia),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

