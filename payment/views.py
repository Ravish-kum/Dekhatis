from api.models import Customer_table
from api.models import Query_table
from django.conf import settings
#from payment.utils import VerifyPaytmResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse, redirect
#from PayTm import Checksum
#import requests

# Create your views here.
#--------------------------------------------------order-----------------------------------------------------------------------------
'''
from . import Checksum
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from payments.utils import VerifyPaytmResponse
import requests


def home(request):
    return HttpResponse("<html><a href='http://localhost:8000/payment'>PayNow</html>")


def payment(request):
    order_id = Checksum.__id_generator__()
    bill_amount = "100"
    data_dict = {
        'MID': settings.PAYTM_MERCHANT_ID,
        'INDUSTRY_TYPE_ID': settings.PAYTM_INDUSTRY_TYPE_ID,
        'WEBSITE': settings.PAYTM_WEBSITE,
        'CHANNEL_ID': settings.PAYTM_CHANNEL_ID,
        'CALLBACK_URL': settings.PAYTM_CALLBACK_URL,
        'MOBILE_NO': '7405505665',
        'EMAIL': 'dhaval.savalia6@gmail.com',
        'CUST_ID': '123123',
        'ORDER_ID':order_id,
        'TXN_AMOUNT': bill_amount,
    } # This data should ideally come from database
    data_dict['CHECKSUMHASH'] = Checksum.generate_checksum(data_dict, settings.PAYTM_MERCHANT_KEY)
    context = {
        'payment_url': settings.PAYTM_PAYMENT_GATEWAY_URL,
        'comany_name': settings.PAYTM_COMPANY_NAME,
        'data_dict': data_dict
    }
    return render(request, 'payments/payment.html', context)


@csrf_exempt
def response(request):
    resp = VerifyPaytmResponse(request)
    if resp['verified']:
        # save success details to db; details in resp['paytm']
        return HttpResponse("<center><h1>Transaction Successful</h1><center>", status=200)
    else:
        # check what happened; details in resp['paytm']
        return HttpResponse("<center><h1>Transaction Failed</h1><center>", status=400)

'''
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
        param_dict ={'MID': 'WorldP64425807474247',#merchant orignal
            'ORDER_ID': 'query.placing_id',
            'TXN_AMOUNT': '1',
            'CUST_ID': 'email',
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',                #contain change
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/woodworks/handlepayment/',}
        checksum = Checksum.generate_checksum(param_dict, MERCHANT)
        #return redirect('payment:query')
        return render(request, 'paytm.html', {'param_dict':param_dict})

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

@csrf_exempt
def handlerequest(request):
    pass