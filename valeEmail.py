
#from email.MIMEImage import MIMEImage
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText # New line
from email.mime.base import MIMEBase
from email import encoders
class sendEmail:
    def __init__(self,password,email):
        self.email=email
        self.password=password

    def enviarEmail(self,email_send):  
        try:
            # Creating a SMTP session | use 587 with TLS, 465 SSL and 25
            server = smtplib.SMTP('smtp.gmail.com', 587)
            context = ssl.create_default_context()
            server.starttls(context=context)
            server.login(self.email, self.password)
            for i in email_send:
                with open(email_send[i][0], 'rb') as ficheiro:
                    msg = MIMEMultipart()
                    msg.attach(MIMEText('Certificado de conclusão de curso','plain'))
                    msg['Subject'] = "Certificados"
                    part=MIMEBase('image','png')
                    part.set_payload(ficheiro.read())
                    part.add_header('Content-Disposition','attachment',filename=email_send[i][0])
                    encoders.encode_base64(part)
                    msg.attach(part)
                    email_body = msg.as_string()
                    server.sendmail(self.email, email_send[i][1], email_body)
            print('Email sent!')
        except Exception as e:
            print(f'Oh no! Something bad happened!n {e}')
        finally:
            print('Closing the server...')
            server.quit()
                