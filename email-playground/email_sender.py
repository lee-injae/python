import smtplib
from email.message import EmailMessage 
from string import Template
from pathlib import Path #os.path 

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Eliza Hamilton'
email['to'] = 'ij@rideartee.com'
email['subject'] = 'Hello World'

# email.set_content('I am a python developer!')
email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('uptownelizahamilton@gmail.com', 'Lin-Manuel$9')
    smtp.send_message(email)
    print('good!')

