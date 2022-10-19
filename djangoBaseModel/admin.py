from django.contrib import admin
from djangoBaseModel.models import YongHu
from djangoBaseModel.models import DianPu
from djangoBaseModel.models import LunBoTu
from djangoBaseModel.models import ShangPin
from djangoBaseModel.models import KeHu
from djangoBaseModel.models import ShouHuoDiZhi
from djangoBaseModel.models import GouWuChe
from djangoBaseModel.models import DingDan
from djangoBaseModel.models import PingJia

# Register your models here.
admin.site.register(YongHu)
admin.site.register(DianPu)
admin.site.register(LunBoTu)
admin.site.register(ShangPin)
admin.site.register(KeHu)
admin.site.register(ShouHuoDiZhi)
admin.site.register(GouWuChe)
admin.site.register(DingDan)
admin.site.register(PingJia)


from django.contrib import admin
admin.site.site_title="后台管理系统"