# Generated by Django 2.0.7 on 2020-04-05 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoBaseModel', '0017_kehu_touxiang'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZaiXianLiuYan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ChenHu', models.CharField(default='', max_length=200, verbose_name='称呼')),
                ('YouXiang', models.CharField(default='', max_length=200, verbose_name='邮箱')),
                ('BiaoTi', models.CharField(default='', max_length=200, verbose_name='标题')),
                ('XinXi', models.CharField(default='', max_length=200, verbose_name='信息')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '在线留言列表',
            },
        ),
    ]
