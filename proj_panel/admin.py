from django.contrib import admin
from proj_panel.models import Order,Foodstall,Request,Order_detail,Item



admin.site.register(Order)
admin.site.register(Order_detail)
admin.site.register(Request)
admin.site.register(Foodstall)
admin.site.register(Item)


# Register your models here.
