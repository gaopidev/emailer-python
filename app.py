#!/usr/bin/python3
'''
App para enviar emails desde cuentas G
Utilizando argparse
'''
import argparse
from email.message import EmailMessage
import ssl
import smtplib

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("para", help="Correo electrónico destinatario")
    parser.add_argument("asunto", help="Asunto del correo")
    parser.add_argument("cuerpo", help="Cuerpo del correo")
    args = parser.parse_args()

    em = EmailMessage()
    email   = "correoejemplo@mail.com"      # Correo electronico del remitente
    pss     = "contrasenasecreta"           # Contraseña del correo remitente
    rece    = args.para                     # Correo electronico que recibe   
    subj    = args.asunto                   # Asunto del correo
    body    = args.cuerpo                   # Cuerpo del mensaje

    em['From']      = email
    em['To']        = rece
    em['subject']   = subj
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email, pss)
        smtp.sendmail(email, rece, em.as_string())
        print("Correo enviado a ", rece)
