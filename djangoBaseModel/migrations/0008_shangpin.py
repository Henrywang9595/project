# Generated by Django 2.0 on 2019-11-14 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoBaseModel', '0007_auto_20191114_2247'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShangPin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShangPinMing', models.CharField(default='', max_length=200, verbose_name='商品名')),
                ('JiaGe', models.CharField(default='', max_length=200, verbose_name='价格')),
                ('JianJie', models.CharField(default='', max_length=200, verbose_name='简介')),
                ('TuPian', models.CharField(default='', max_length=200, verbose_name='图片')),
                ('LeiXing', models.CharField(default='', max_length=200, verbose_name='类型')),
                ('ShuLiang', models.CharField(default='', max_length=200, verbose_name='数量')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '商品列表',
            },
        ),
    ]