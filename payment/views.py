from api.models import Customer_table
from api.models import Query_table

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
#--------------------------------------------------order-----------------------------------------------------------------------------

def credentials(request):                                     
                                                #order table made for query generation
    if request.method == 'GET': 
        return render(request,'credentials.html')
    else: 
        postdata =request.POST
        name = postdata.get('name')
        phone= postdata.get('phone')
        address = postdata.get('address')
        pin = postdata.get('pin')
        email= postdata.get('email')
        password= postdata.get('password')
        customer= Customer_table(
                           customer_name=name,
                           customer_phone=phone,
                           customer_address=address,
                           customer_pin=pin,
                           customer_email=email,
                           customer_pass=password
                           )
        customer.save()     
        return redirect('payment:query')

def query(request):
    if request.method == 'GET':
        return render(request,'final_result.html')
    else:
        postdata =request.POST
        placing_id = postdata.get('placing_id')
        customer_id = postdata.get('customer_id')
        shop_id= postdata.get('shop_id')
        item_id = postdata.get('item_id')
        item_cost = postdata.get('item_cost')
        item_revenue= postdata.get('item_revenue')
        order_date= postdata.get('order_date')
        order_status= postdata.get('order_status')
        transcation_id= postdata.get('transaction_id')

        query= Query_table(
                        placing_id=placing_id,
                        customer_id=customer_id,
                        shop_id=shop_id,
                        item_id=item_id,
                        item_cost=item_cost,
                        item_revenue=item_revenue,
                        order_date=order_date,
                        order_status=order_status,
                        transcation_id=transcation_id,

                            )
        query.save()     
