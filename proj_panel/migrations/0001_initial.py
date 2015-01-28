# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foodstall',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order_details',
            fields=[
                ('item_id', models.OneToOneField(to='proj_panel.Items', serialize=False, primary_key=True)),
                ('quant', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('date_time_added', models.DateTimeField(verbose_name='time order placed')),
                ('stat', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('approved', models.IntegerField()),
                ('item_id', models.IntegerField()),
                ('quant', models.IntegerField()),
                ('order_details_id', models.IntegerField()),
                ('order_id', models.ForeignKey(to='proj_panel.Orders')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('passwd', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='orders',
            name='cust_id',
            field=models.ForeignKey(to='proj_panel.Users'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order_details',
            name='order_id',
            field=models.ForeignKey(to='proj_panel.Orders'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='items',
            name='foodstall_id',
            field=models.ForeignKey(to='proj_panel.Foodstall'),
            preserve_default=True,
        ),
    ]
