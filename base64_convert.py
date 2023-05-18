from settings import *

def convert(data):
    msg = data.encode('ascii')
    return base64.b64encode(msg).decode('ascii')