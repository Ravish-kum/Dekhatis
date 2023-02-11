from django.contrib import admin
from .models import Product
from .models import Shop_table
from .models import Customer_table
from .models import Query_table

# Register your models here.
admin.site.register(Product)
admin.site.register(Shop_table)
admin.site.register(Customer_table)
admin.site.register(Query_table)
