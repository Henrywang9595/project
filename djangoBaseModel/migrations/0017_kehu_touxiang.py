# Generated by Django 2.1.7 on 2019-12-28 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoBaseModel', '0016_pingjia'),
    ]

    operations = [
        migrations.AddField(
            model_name='kehu',
            name='TouXiang',
            field=models.CharField(default='', max_length=200, verbose_name='头像'),
        ),
    ]
