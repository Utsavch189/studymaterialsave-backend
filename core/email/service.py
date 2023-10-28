from .mail import Email
from ..utils.threads.thread import Thread

class EmailService:

    def __init__(self,subject:str,mail_sender:str,mail_receiver:str,template:str,context:str) -> None:
        self.mail=Email(subject,mail_sender,mail_receiver,template,context)
    
    def send(self):
        return Thread(inst=self.mail).start()
    
