# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proj_panel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('date_time_added', models.DateTimeField(verbose_name='time order placed')),
                ('stat', models.IntegerField(default=0)),
                ('cust_id', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order_detail',
            fields=[
                ('item_id', models.OneToOneField(to='proj_panel.Item', primary_key=True, serialize=False)),
                ('quant', models.IntegerField()),
                ('order_id', models.ForeignKey(to='proj_panel.Order')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('approved', models.IntegerField()),
                ('item_id', models.IntegerField()),
                ('quant', models.IntegerField()),
                ('order_details_id', models.IntegerField()),
                ('order_id', models.ForeignKey(to='proj_panel.Order')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='items',
            name='foodstall_id',
        ),
        migrations.RemoveField(
            model_name='order_details',
            name='item_id',
        ),
        migrations.DeleteModel(
            name='Items',
        ),
        migrations.RemoveField(
            model_name='order_details',
            name='order_id',
        ),
        migrations.DeleteModel(
            name='Order_details',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='cust_id',
        ),
        migrations.RemoveField(
            model_name='requests',
            name='order_id',
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
        migrations.DeleteModel(
            name='Requests',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.AddField(
            model_name='item',
            name='foodstall_id',
            field=models.ForeignKey(to='proj_panel.Foodstall'),
            preserve_default=True,
        ),
    ]
