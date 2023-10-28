from django.template.loader import get_template
from django.core.mail import send_mail,EmailMessage


class Email:

    def __init__(self,subject:str,mail_sender:str,mail_receiver:str,template:str,context:str) -> None:
        self.subject=subject
        self.mail_sender=mail_sender
        self.mail_receiver=mail_receiver
        self.templates = get_template(template).render(context)
    
    def sends(self):
        try:
            
            email=EmailMessage(self.subject,self.templates,self.mail_sender,[self.mail_receiver])
            email.content_subtype = "html"
            email.send()
        except Exception as e:
            raise Exception(str(e))