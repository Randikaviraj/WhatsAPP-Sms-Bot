import requests
import os
from dotenv import load_dotenv

def sendMessage(reciverNumber,msg,send_msg_chat_api_url):
    payload = {"phone": reciverNumber, "body": msg}
    r = requests.post(send_msg_chat_api_url, data=payload)
    if r.status_code==200:
      return True
    return False

if __name__=="__main__":
    try:
        load_dotenv()
        send_msg_chat_api_url = os.getenv('send_msg_chat_api_url')
        print("Hello !")
        reciver=input("Enter your reciver number :")
        while True:
            msg=input("Enter your message (quit)for exit :")
            if msg=="quit":
              break
            if sendMessage(reciver,msg,send_msg_chat_api_url):
                print("Successfully send message")
            else:
                print("Something wrong send faild")    
    except:
      print('An exception occurred')