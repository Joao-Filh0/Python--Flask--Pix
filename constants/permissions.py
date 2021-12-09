import  os, base64


__path = os.path.dirname(os.path.realpath(__file__))


def __credentalsPath(credential):
    path = os.path.join(__path,"data")
    return os.path.join(path,credential)

def __base_Basic(client_id,client_secret):
    crd = f"{client_id}:{client_secret}"
    message_bytes = crd.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    basic_auth = base64_bytes.decode('ascii')
    return f"Basic {basic_auth}"


__CLIENT_ID__ = "Cole aqui seu CLIENT_ID"
__CLIENT_SECRET__ = "Cole Aqui seu CLIENT_SECRET"


CERTIFICATES = (__credentalsPath("Seu arquivo .pem"),__credentalsPath("Seu Arquivo .key"))

BASIC_CREDENTIAL = __base_Basic(__CLIENT_ID__,__CLIENT_SECRET__)







    
