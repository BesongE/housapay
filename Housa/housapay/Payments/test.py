import time
import uuid
from cinetpay_sdk.s_d_k import Cinetpay

apikey = '93041234866ba2b2e6dc553.14396706'
site_id = '5877754'

client = Cinetpay(apikey=apikey, site_id=site_id)

tx_id = str(uuid.uuid4())
return_url = ''
notify_url = ''
channels = 'MOBILE_MONEY'
data = {
            'amount': 500,
            'currency':'XAF',
            'transaction_id':tx_id,
            'description': 'Test Request',
            'return_url':'',
            'notify_url':'',
            'customer_name':'Besong',
            'customer_surname':'Eustess',
        }

r = client.PaymentInitialization(data)

print('transaction_ID: '+tx_id)
print(r)
verify = client.TransactionVerfication_token('79f0f189e39c9204de8875d1208a985b86a570430a41d1f99bbaa735d8b144a38e408fb0e3d1495ba01221778d3399d6f968c531940e3d')
time.sleep(2.0)
print(verify)




# res = req.get('https://google.com').json()
# data = res
# # print(data)
# version = ''
# version1 = 'v_1.0/'
# version2 = 'v_1.1/'

# url = 'https://www.google.com/'
# path = 'api/get/users/' 
# full_endpoint = f"{url}{version1}{path}"
# print(full_endpoint)