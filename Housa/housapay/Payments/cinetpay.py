from email.charset import BASE64
from urllib import response
import uuid
import requests
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# from Housa.Housa.settings import BASE_DIR


class CinetPay:
    def __init__(self):
        self.apikey = '93041234866ba2b2e6dc553.14396706'
        self.site_id = '5877754'
        self.notify_url = str
        self.return_url = BASE_DIR
        self.mode = str
        self.tx_id = str(uuid.uuid4())
        self.currency = 'XAF'
        self.channels = 'MOBILE_MONEY'
        self.cus_id=str
        self.cus_country="CM"
    

    def cardpay(self, amt:int, cus_name:str, cus_surname:str, cus_email:str, cus_tel:str, cus_addr:str, cus_city:str, cus_country:str, cus_state, cus_zip:str, reason:str):
        headers = {
            'Content-Type':'application/json',
            }
        url = 'http://api-checkout.cinetpay.com/v2.payment'

        data = {
            'apikey': self.apikey,
            'site_id':self.site_id,
            'transaction_id':self.tx_id,
            'amount': amt,
            'currency':self.currency,
            'description': reason,
            'customer_id':self.cus_id,
            'customer_name':cus_name,
            'customer_surname':cus_surname,
            'customer_email':cus_email,
            'customer_phone_number':cus_tel,
            'customer_address':cus_addr,
            'customer_city':cus_city,
            'customer_country':cus_country,
            'customer_state':cus_state,
            'customer_zip_code': cus_zip,
            'notify_url': self.notify_url,
            'return_url':self.return_url,
            'channels':'ALL'
        }

        response = requests.request(method="post", url=url, headers=headers, data=data)
        response = response.json()
        print(response)
        return response

    def paymomo(self, amt:int, cus_name:str, cus_email:str, cus_tel:str, reason:str):
        headers = {
            'Content-Type':'application/json',
            }
        url = 'http://api-checkout.cinetpay.com/v2/payment'

        data = {
            'apikey': self.apikey,
            'site_id':self.site_id,
            'transaction_id':self.tx_id,
            'amount': amt,
            'currency':self.currency,
            'description': reason,
            'customer_id':self.cus_id,
            'customer_name':cus_name,
            'customer_email':cus_email,
            'customer_phone_number':str(cus_tel).startswith('+237'),
            'notify_url': self.notify_url,
            'return_url':self.return_url,
            'channels':self.channels
        }

        response = requests.request(method="post", url=url, headers=headers, data=data)
        response = response.json()
        print(response)
        return response
    
    def verify(self, tx_id):
        url = 'http://api-checkout.cinetpay.com/v2/payment/verify'
        header={'Content-Type':'application/json'}
        response = requests.request(method='post',url=url,headers=header,data={'transaction_id':self.tx_id})
        response.json()
        return response


# payment = CinetPay().tx_id
# payment2 = CinetPay()
# payment2.paymomo(5000,'Besong','eustessb@gmail.com','+237673199382','Advance rent')
# print(payment2.tx_id)
# print(payment2.pay(200, 'My rent for this month'))

# print(BASE_DIR)