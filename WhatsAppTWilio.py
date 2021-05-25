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
    

