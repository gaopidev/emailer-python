#!/usr/bin/python3
'''
App para enviar emails desde cuentas G
'''
import sys
from email.message import EmailMessage
import ssl
import smtplib

if __name__ == "__main__":

    if len(sys.argv) == 4:
        
        em = EmailMessage()

        email   = "example@mail.com"            # Correo electronico del remitente
        pss     = "secret_password_of_email"    # Contraseña del correo remitente
        rece    = sys.argv[1]                   # Correo electronico que recibe   
        subj    = sys.argv[2]                   # Asunto del correo
        body    = sys.argv[3]                   # Cuerpo del mensaje

        em['From']      = email
        em['To']        = rece
        em['subject']   = subj
        em.set_content(body)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email, pss)
            smtp.sendmail(email, rece, em.as_string())
            print("Correo enviado! a ", rece)
    else:
        print("Error")
        print("Uso: python3 app.py [mail_para] [asunto] [mensaje]")
