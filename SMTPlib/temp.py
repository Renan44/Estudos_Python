from string import Template
from datetime import datetime
from dados_email import meu_email, minha_senha

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

with open('template.html', 'r') as html:
    template = Template(html.read())
    data_de_hoje = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.safe_substitute(nome=Nome_do_cliente, data=data_de_hoje)

msg = MIMEMultipart()
msg['from'] = 'Renan'
msg['to'] = Email_do_Cliente
msg['subject'] = 'E-mail de teste.'
corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with open('imagem.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP('smtp.gmail.com', port =587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(meu_email,minha_senha)
    smtp.send_message(msg)
    print("E-mail enviado")