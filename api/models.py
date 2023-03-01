from django.db import models

# Create your models here.

class Product(models.Model):
    item_id = models.CharField(max_length=30,primary_key = True )
    m_item_id = models.CharField(max_length=30, blank=True)
    item_name = models.CharField(max_length=50)
    item_image = models.ImageField(upload_to='uploads/images')
    item_categories = models.CharField(max_length=30)
    item_detail= models.CharField(max_length=300)
    item_cost = models.IntegerField()
    item_revenue = models.IntegerField()
    shop_pin= models.IntegerField()
    shop_id= models.ForeignKey("Shop_table", verbose_name= "placer",default=1, on_delete=models.SET_DEFAULT)
    item_size = models.CharField(max_length=30,blank=True)
    item_finish = models.CharField(max_length=30,blank=True)
    item_storage = models.CharField(max_length=30,blank=True)
    item_colour = models.CharField(max_length=30,blank=True)
    item_shipping_time = models.CharField(max_length=30)
    item_visual_similarity= models.CharField(max_length=30,blank=True)
    item_warrenty = models.CharField(max_length=30,blank=True)
    item_instructions = models.CharField(max_length=30,blank=True)
    item_rating = models.IntegerField(default=0)
    class Meta:
        db_table='product'

class Shop_table(models.Model):
    shop_id= models.CharField(max_length=30,primary_key = True )
    shop_name= models.CharField(max_length=45)
    shop_brand_name= models.CharField(max_length=45,blank=True)
    shop_email= models.EmailField()
    shop_pass= models.CharField(max_length=200, unique=True,blank=True)
    shop_address= models.CharField(max_length=300)
    shop_phone= models.CharField(max_length=14)
    shop_alt= models.CharField(max_length=14)
    shop_pin= models.IntegerField()
    manufacturer_name= models.CharField(max_length=45)
    manufacturer_address =models.CharField(max_length=45)
    manufacturer_phone =models.IntegerField(default=0)
    shop_ordered= models.CharField(max_length=50,blank=True)
    class Meta:
        db_table='shop_table'

class Customer_table(models.Model):
    customer_id= models.AutoField(primary_key = True )
    customer_name= models.CharField(max_length=45)
    customer_email= models.EmailField()
    customer_otp= models.CharField(max_length=20,blank=True)
    customer_state= models.CharField(max_length=200,blank=True)
    customer_address= models.CharField(max_length=300,blank=True)
    customer_pin =models.IntegerField(default=0)
    customer_phone= models.CharField(max_length=14,blank=True)
    customer_cerdits_tokens= models.IntegerField(default= 0)
    class Meta:
        db_table='customer_table'


class Query_table(models.Model):
    placing_id = models.CharField(max_length=50,primary_key=True)
    customer_id= models.ForeignKey("Customer_table", verbose_name= "customer",default=1, on_delete=models.SET_DEFAULT)
    shop_id = models.ForeignKey("Shop_table", verbose_name= "shop", default=1,on_delete=models.SET_DEFAULT)
    item_id = models.ForeignKey("Product", verbose_name= "item",default=1, on_delete=models.SET_DEFAULT)
    item_cost = models.IntegerField()
    item_revenue = models.IntegerField()
    order_date= models.DateField()
    order_status = models.CharField(max_length=100)
    transcation_id = models.CharField(max_length=200)
    bank_id=models.CharField(max_length=200,blank=True)
    class Meta:
        db_table='query_table'

class Images_table(models.Model):
    item_id = models.ForeignKey("Product", verbose_name= "item", default=1, on_delete=models.SET_DEFAULT)
    item_pic1 = models.ImageField(upload_to='uploads/images',blank=True)
    item_pic2 = models.ImageField(upload_to='uploads/images',blank=True)
    item_pic3 = models.ImageField(upload_to='uploads/images',blank=True)
    item_pic4 = models.ImageField(upload_to='uploads/images',blank=True)
    item_pic5 = models.ImageField(upload_to='uploads/images',blank=True)
    item_pic6 = models.ImageField(upload_to='uploads/images',blank=True)
    item_pic7 = models.ImageField(upload_to='uploads/images',blank=True)
    item_pic8= models.ImageField(upload_to='uploads/images',blank=True)
    item_pic9 = models.ImageField(upload_to='uploads/images',blank=True)
    item_pic10 = models.ImageField(upload_to='uploads/images',blank=True)
    class Meta:
         db_table='images_table'

class Advertisement_table(models.Model):
    adver_image =models.ImageField(upload_to='uploads/adver_images')
    adver_url =models.CharField(max_length=100)
    class Meta:
        db_table='advertisement_table'

class Review_table(models.Model):
    customer_id= models.ForeignKey("Customer_table", verbose_name= "customer", default=1, on_delete=models.SET_DEFAULT)
    comments= models.CharField(max_length=400)
    events=models.ImageField(upload_to='uploads/reviews_images')
    class Meta:
        db_table='review_table'

class Cancellations_table(models.Model):
    cancellation_id= models.CharField(max_length=100)
    placing_id= models.ForeignKey("Customer_table", verbose_name= "customer", default=1, on_delete=models.SET_DEFAULT)
    shop_id = models.ForeignKey("Shop_table", verbose_name= "shop", default=1, on_delete=models.SET_DEFAULT)
    item_id = models.ForeignKey("Product", verbose_name= "item", default=1, on_delete=models.SET_DEFAULT)
    cancellations_date= models.DateField(default=None)
    order_date= models.CharField(max_length=50)
    order_status = models.CharField(max_length=100)
    transcation_id = models.CharField(max_length=200)
    bank_id=models.CharField(max_length=200)
    class Meta:
        db_table='cancellations_table'

