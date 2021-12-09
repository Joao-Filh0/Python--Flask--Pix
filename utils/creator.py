import libscrc
from datetime import datetime
from random import randint,choice


def txid(userID):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    now = str(datetime.now()).replace("-",'').replace(".",'').replace(":",'').replace(" ",'')[2:14]
    byts = bytes(userID, 'utf-8')
    userID = hex(libscrc.xmodem(byts,0xFFFF)).upper().replace("0X","")
     
    id = ""
    for i in range(0,15):
        sort = randint(0,9)

        if(randint(0,len(id))%2 ==0):
            id = id+str(sort)
        else:
            sort = randint(0,25)
            if(sort%2==0):
                id = id+choice(alphabet).upper()
            else:
                id = id+choice(alphabet)
    return userID+now+id

