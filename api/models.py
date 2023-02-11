from django.db import models

# Create your models here.

class Product(models.Model):
    item_id = models.CharField(max_length=30,primary_key = True )
    c_item_id = models.CharField(max_length=30)
    item_name = models.CharField(max_length=50)
    item_image = models.ImageField(upload_to='uploads/images')
    item_categories = models.CharField(max_length=30)
    item_detail= models.CharField(max_length=300)
    item_cost = models.IntegerField()
    item_revenue = models.IntegerField()
    shop_pin= models.IntegerField()
    shop_id= models.ForeignKey("Shop_table", verbose_name= "placer", default=1, on_delete=models.SET_DEFAULT)
    class Meta:
        db_table='product'

class Shop_table(models.Model):
    shop_id= models.CharField(max_length=30,primary_key = True )
    shop_name= models.CharField(max_length=45)
    shop_email= models.EmailField()
    shop_pass= models.CharField(max_length=200, unique=True)
    shop_address= models.CharField(max_length=300)
    shop_phone= models.CharField(max_length=14)
    shop_alt= models.CharField(max_length=14)
    shop_pin= models.IntegerField()
    shop_ordered= models.CharField(max_length=50)
    class Meta:
        db_table='shop_table'

class Customer_table(models.Model):
    customer_id= models.AutoField(primary_key = True )
    customer_name= models.CharField(max_length=45)
    customer_email= models.EmailField()
    customer_pass= models.CharField(max_length=200, unique=True)
    customer_address= models.CharField(max_length=300)
    customer_pin =models.IntegerField(default=0)
    customer_phone= models.CharField(max_length=14)
    class Meta:
        db_table='customer_table'


class Query_table(models.Model):
    placing_id = models.CharField(max_length=50,primary_key=True)
    customer_id= models.ForeignKey("Customer_table", verbose_name= "customer", default=1, on_delete=models.SET_DEFAULT)
    shop_id = models.ForeignKey("Shop_table", verbose_name= "shop", default=1, on_delete=models.SET_DEFAULT)
    item_id = models.ForeignKey("Product", verbose_name= "item", default=1, on_delete=models.SET_DEFAULT)
    item_cost = models.IntegerField()
    item_revenue = models.IntegerField()
    order_date= models.DateField()
    order_status = models.CharField(max_length=100)
    transcation_id = models.CharField(max_length=200)

    class Meta:
        db_table='query_table'
