# Generated by Django 2.0 on 2019-11-14 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoBaseModel', '0005_auto_20191114_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dianpu',
            name='ZhuangTai',
            field=models.CharField(default='禁用', max_length=200, verbose_name='状态'),
        ),
    ]
