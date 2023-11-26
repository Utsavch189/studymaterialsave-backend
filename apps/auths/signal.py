from .models.user import User
from django.db.models.signals import post_save
from core.email.service import EmailService
from django.dispatch import receiver

@receiver(post_save,sender=User)
def post_signals(sender,instance,**kwargs):
    print('post_save>>>>>>')
    context={
        "name":instance.full_name,
        "header":"Account Created Successfully!",
        "body":f"Save Your Study Materials now effectively!</br> <b>Username : {instance.username}</b>"
    }
    email=EmailService(
        subject="Thank You For Account Creation!",
        mail_sender="utsavpokemon9000chatterjee@gmail.com",
        mail_receiver=instance.email,
        template='mail.html',
        context=context
    )
    email.send()