from locale import currency
from os import error
import requests 
from traceback import print_stack
from django.http.request import HttpRequest

tx_ref = ''
amount = ''
currency = 'XAF'
redirect_url = ''
customer_email = ''
customer_name = ''
customer_tel = ''
custom_pay_title = 'Housa MoMo Pay'
secret_key = ''

try:
    response = requests.post(
        url='https://api.flutterwave.com/v3/payments',
        data=[
            {
            'tx_ref':tx_ref,
            'amount':amount,
            'currency':currency,
            'redirect_url':redirect_url,
            'customer':{
                'email':customer_email,
                'name': customer_name,
                'phonenumber':customer_tel,
            },
            'customizations': {
                'title':custom_pay_title
            },
        }],
        headers={
                'Authorization': f"Bearer {secret_key}",
                'Content-Type': 'application/json'
            }
        )
    print(response)

except error:
    pass