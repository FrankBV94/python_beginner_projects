# Ir a la cuenta de gmail y activar la atenticacion en 2 pasos
# Generar la contraseña
# Crear la funcion para mandar el correo

from email.message import EmailMessage
import ssl
import smtplib

email_sender = "frankbotelle@gmail.com"
email_password = "kjvrotsbxscbihdy"
email_receiver = "alugoa@udio.cujae.edu.cu"
email_subject = "Aloha"
email_body = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore 
et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo 
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""


em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = email_subject
em.set_content(email_body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string)
