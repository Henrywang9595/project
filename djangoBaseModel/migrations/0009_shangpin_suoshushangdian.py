# Generated by Django 2.0 on 2019-11-14 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoBaseModel', '0008_shangpin'),
    ]

    operations = [
        migrations.AddField(
            model_name='shangpin',
            name='SuoShuShangDian',
            field=models.CharField(default='', max_length=200, verbose_name='ζε±εεΊ'),
        ),
    ]
