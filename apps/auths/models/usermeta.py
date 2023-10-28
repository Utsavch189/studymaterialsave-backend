from .user import User
from django.db import models
from datetime import datetime

class UserMeta(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_meta')
    meta_id=models.CharField(max_length=100,primary_key=True,default="")
    profile_pic_url=models.CharField(max_length=50,null=True,blank=True)
    bio=models.TextField(blank=True,null=True)
    doj=models.DateTimeField(default=datetime.now())

    def __str__(self) -> str:
        return self.user.full_name
