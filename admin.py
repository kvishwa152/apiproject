from django.contrib import admin
from .models import ProductModel

# Register your models here.
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['prd_id','prd_name','prd_qnt','prd_price']


admin.site.register(ProductModel,ProductModelAdmin)