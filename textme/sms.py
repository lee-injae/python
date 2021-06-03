from twilio.rest import Client 
 
account_sid = 'AC42fe612fbaeff1a5f1e152e73af4738c' 
auth_token = '[AuthToken]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MG01151a06da6d7aabc4c4afd8e1ca1f56',       
                              body='this is so COOL',
                              to='+19999999839' 
                          ) 
 
print(message.sid)