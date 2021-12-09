
import libscrc #Lib externa

def build_payload(data):

    len_intro_id = f"0014br.gov.bcb.pix25{str(len(data['location'])).zfill(2)}{data['location']}"
     

    id_00 = "000201"
    id_26 = f"26{str(len(len_intro_id)).zfill(2)}{len_intro_id}"
    id_52 =  f"52040000"
    id_53 = "5303986"
    id_58 = "5802BR"
    id_59 = f"59{str(len('Rifas')).zfill(2)}{'Rifas'}"
    id_60 = f"60{str(len('Camacari')).zfill(2)}{'Camacari'}"
    id_61 = "62070503***"
    payload = id_00+id_26+id_52+id_53+id_58+id_59+id_60+id_61+"6304"
    byts = bytes(payload, 'utf-8')
    checksum = hex(libscrc.xmodem(byts,0xFFFF)).upper().replace("0X","")
     
    return payload+checksum



