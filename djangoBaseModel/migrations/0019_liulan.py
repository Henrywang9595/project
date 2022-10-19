# Generated by Django 2.0.7 on 2020-05-03 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoBaseModel', '0018_zaixianliuyan'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiuLan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShangPinMing', models.CharField(default='', max_length=200, verbose_name='商品名')),
                ('JiaGe', models.CharField(default='', max_length=200, verbose_name='价格')),
                ('JianJie', models.CharField(default='', max_length=200, verbose_name='简介')),
                ('TuPian', models.CharField(default='', max_length=200, verbose_name='图片')),
                ('LeiXing', models.CharField(default='', max_length=200, verbose_name='类型')),
                ('ShuLiang', models.CharField(default='', max_length=200, verbose_name='数量')),
                ('SuoShuShangDian', models.CharField(default='', max_length=200, verbose_name='所属商店')),
                ('LiuLanRen', models.CharField(default='', max_length=200, verbose_name='浏览人')),
                ('LiuLanShiJian', models.CharField(default='', max_length=200, verbose_name='浏览时间')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '浏览列表',
            },
        ),
    ]
