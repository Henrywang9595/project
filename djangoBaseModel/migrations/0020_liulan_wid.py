# Generated by Django 2.0.7 on 2020-05-03 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoBaseModel', '0019_liulan'),
    ]

    operations = [
        migrations.AddField(
            model_name='liulan',
            name='wid',
            field=models.CharField(default='', max_length=200, verbose_name='物品id'),
        ),
    ]
