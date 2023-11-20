
import os,sys
import smtplib
import ssl


from pybars import Compiler
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


compiler = Compiler()



def sendEmail(template, to, subj, fields,replyTo=None):
    templateFile = open(os.path.join(os.path.dirname(__file__),'email_templates',''+template+'.handlebars'),"r", encoding="utf-8")
    source = templateFile.read()
    template = compiler.compile(source)
    if (os.getenv("SMTP_TESTING") == True or (os.getenv("SMTP_TESTING") is not None and os.getenv("SMTP_TESTING") != False)):
        print(to, subj, template(fields))
    else:
        performSmtpSend(to, subj,template(fields),replyTo)

def performSmtpSend(to,subj,body,replyTo):
    if os.getenv("SMTP_MAILADRESS") is not None:
        sender_mail = os.getenv("SMTP_MAILADRESS")
    else:
        sender_mail = os.getenv("SMTP_USERNAME")
    message = MIMEMultipart("alternative")
    message["Subject"] = subj
    message["From"] = sender_mail
    message["To"] = to
    if replyTo is not None:
        message.add_header('reply-to', replyTo)
    mailBody = MIMEText(body, "html")
    message.attach(mailBody)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    server =  smtplib.SMTP_SSL(os.getenv("SMTP_SERVER"), os.getenv("SMTP_PORT"), context=context) 
    try:
        server.login(os.getenv("SMTP_USERNAME"), os.getenv("SMTP_PASSWORD"))
        server.sendmail(
            sender_mail, to, message.as_string()
        )
    except:
        print ("Unknown error:", sys.exc_info()[0])
    finally:
        server.quit()