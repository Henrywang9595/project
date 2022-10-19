# Generated by Django 2.0 on 2019-11-14 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoBaseModel', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='DianPu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DianPuMing', models.CharField(default='', max_length=20, verbose_name='店铺名')),
                ('JianJie', models.CharField(default='', max_length=20, verbose_name='简介')),
                ('YongYouZhe', models.CharField(default='', max_length=20, verbose_name='拥有者')),
                ('ZhaoPai', models.CharField(default='', max_length=20, verbose_name='招牌')),
                ('ZhuangTai', models.CharField(default='', max_length=20, verbose_name='状态')),
                ('ShiFuTongGuo', models.CharField(default='', max_length=20, verbose_name='是否通过')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '商家列表',
            },
        ),
        migrations.CreateModel(
            name='LunBoTu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TuPian', models.CharField(default='', max_length=20, verbose_name='图片')),
                ('LianJie', models.CharField(default='', max_length=20, verbose_name='链接')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '轮播图列表',
            },
        ),
        migrations.CreateModel(
            name='YongHu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ZhangHao', models.CharField(default='', max_length=20, unique=True, verbose_name='账号')),
                ('MiMa', models.CharField(default='', max_length=20, verbose_name='密码')),
                ('XingMing', models.CharField(default='', max_length=20, verbose_name='姓名')),
                ('XingBie', models.CharField(default='', max_length=20, verbose_name='性别')),
                ('NianLing', models.CharField(default='', max_length=20, verbose_name='年龄')),
                ('JiGuan', models.CharField(default='', max_length=20, verbose_name='籍贯')),
                ('MinZu', models.CharField(default='', max_length=20, verbose_name='民族')),
                ('TouXiang', models.CharField(default='', max_length=20, verbose_name='头像')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '用户列表',
            },
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
