from django.db import models
from django.contrib.auth.models import User




class Order(models.Model):
	cust_id = models.ForeignKey(User, unique=True)
	date_time_added = models.DateTimeField('time order placed')
	stat = models.IntegerField(default=0)


class Request(models.Model):
	order_id = models.ForeignKey(Order)
	approved = models.IntegerField()
	item_id = models.IntegerField()
	quant = models.IntegerField()
	order_details_id = models.IntegerField()

class Foodstall(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Item(models.Model):
	name = models.CharField(max_length=200)
	foodstall_id = models.ForeignKey(Foodstall)
	desc = models.CharField(max_length=500)
	price = models.IntegerField()
	def __str__(self):
		return self.name

class Order_detail(models.Model):
	order_id = models.ForeignKey(Order)
	item_id = models.OneToOneField(Item, primary_key=True)
	quant = models.IntegerField()






# Create your models here.
