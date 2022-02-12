from string import Template
from datetime import datetime 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

email = "..."
senha = "..."

with open('/home/mack/Documents/code/python/template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.safe_substitute(nome = 'Allison', data = data_atual)

msg = MIMEMultipart()
msg['from'] = 'Allison Eduardo'
msg['to'] = email
msg['subject'] = 'Email de teste'

corpo = MIMEText(corpo_msg, 'html')

msg.attach(corpo)

with smtplib.SMTP(host='smtp.live.com', port=25) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(email, senha)
    smtp.send_message(msg)
    print('E-mail enviado com sucesso')