from django.db import models

# Create your models here.
class ProductModel(models.Model):
    prd_id = models.IntegerField(primary_key=True)
    prd_name = models.CharField(max_length=255)
    prd_qnt = models.IntegerField()
    prd_price = models.IntegerField()

