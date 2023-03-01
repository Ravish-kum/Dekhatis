from django.contrib import admin
from .models import Product
from .models import Shop_table
from .models import Customer_table
from .models import Query_table
from .models import Images_table
from .models import Advertisement_table
from .models import Review_table
from .models import Cancellations_table
#from .models import Product_varient_table

# Register your models here.
admin.site.register(Product)
admin.site.register(Shop_table)
admin.site.register(Customer_table)
admin.site.register(Images_table)
admin.site.register(Advertisement_table)
admin.site.register(Review_table)
admin.site.register(Cancellations_table)
#admin.site.register(Product_varient_table)
admin.site.register(Query_table)
