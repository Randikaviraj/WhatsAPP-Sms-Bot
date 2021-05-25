from twilio.rest import Client 
import os
from dotenv import load_dotenv
 
def sendMessage(sender,reciver,msg,account_sid,auth_token):

    client = Client(account_sid, auth_token) 
 
    message = client.messages.create( 
                              from_='whatsapp:'+sender,  
                              body=msg,      
                              to='whatsapp:'+reciver
                          ) 
 
    print(message.sid)
    
# +14155238886   
if __name__=="__main__":
    try:
        account_sid = os.getenv('account_sid')
        auth_token = os.getenv('auth_token')
        print("Hello !")
        sender=input("Enter your sender number :")
        reciver=input("Enter your reciver number :")
        msg=input("Enter your message :")
        sendMessage(sender,reciver,msg,account_sid,auth_token)
    except:
      print('An exception occurred')
