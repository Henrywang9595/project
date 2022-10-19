from django.shortcuts import render
from django.shortcuts import render, render_to_response


def shangpingsousuojieguo(request):
    return render(request, 'shangpingsousuojieguo.html')

def index(request):
    return render(request, 'index.html')

def zaixianliuyan(request):
    return render(request, 'zaixianliuyan.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def regist(request):
    return render(request, 'regist.html')


def daoru(request):
    return render(request, 'daoru.html')

def main(request):
    return render(request, 'main.html')

def main2(request):
    return render(request, 'main2.html')

def data(request):
    return render(request, 'data.html')

def dianpulist(request):
    return render(request, 'dianpulist.html')
def shangpinglist(request):
    return render(request, 'shangpinglist.html')

def shouye(request):
    return render(request, 'shouye.html')
def shangpingliebiao(request):
    return render(request, 'shangpingliebiao.html')
def shangpingxiangqing(request):
    return render(request, 'shangpingxiangqing.html')
def wodedingdan(request):
    return render(request, 'wodedingdan.html')

def gouwuche(request):
    return render(request, 'gouwuche.html')
def ShouHuoDiZhi(request):
    return render(request, 'shouhuodizhi.html')

def dingdanliebiaohoutai(request):
    return render(request, 'dingdanliebiaohoutai.html')

def yonghudenglu(request):
    return render(request, 'yonghudenglu.html')

def hou(request):
    return render(request, 'hou.html')

def userCenter(request):
    return render(request, 'userCenter.html')

