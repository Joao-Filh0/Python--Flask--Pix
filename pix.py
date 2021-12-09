import json,requests
from constants import permissions
from constants import urls
from constants import body
from utils import qrcode
from utils import creator




class PixModel:
    def __init__(self):
        #Auth para pegar token de acesso
        self.ACESS_TOKEN = self.auth(body.cob_data).get("access_token")
       



    def auth(self,data):
        r = requests.post(url= urls.auth_url,
                          data = json.dumps(data) ,
                          headers = {'content-type': 'application/json',
                                    'Authorization':  permissions.BASIC_CREDENTIAL},
                                    cert= permissions.CERTIFICATES)
        return json.loads(r.text)
        

    def cob(self,uid,data):
        txid =creator.txid(uid)
        r = requests.put(url= urls.cob_url+txid,
        data=json.dumps(data),
        headers={'content-type': 'application/json',
                                    'Authorization': f"Bearer {self.ACESS_TOKEN}"},
                                    cert= permissions.CERTIFICATES)
        response = json.loads(r.text)
        if(r.status_code == 201):
          self.webhooks_config(key=response.get("chave"))
          return {
            "txid" : txid,
            "qr_code" : qrcode.build_payload(response)
          }
        return {}

    def webhooks_config(self,key):
      
      requests.put(url= urls.webhooks_config_url+key,data=json.dumps(body.webhook_data),
      headers={'content-type': 'application/json',
                                    'Authorization': f"Bearer {self.ACESS_TOKEN}"},
                                    cert= permissions.CERTIFICATES)
      return 

      
    
    
           











   
        

