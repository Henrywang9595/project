# Generated by Django 2.0 on 2019-11-21 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoBaseModel', '0010_kehu'),
    ]

    operations = [
        migrations.AddField(
            model_name='dianpu',
            name='leixing',
            field=models.CharField(default='', max_length=200, verbose_name='类型'),
        ),
    ]
