from .user import User
from django.db import models

class ProfilePicMeta(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile_pic_meta')
    profile_pic_meta_id=models.CharField(max_length=100,primary_key=True,default="")
    picture_name=models.CharField(max_length=50,null=True,blank=True)
    public_id=models.CharField(max_length=50,null=True,blank=True)
    resource_type=models.CharField(max_length=50,null=True,blank=True)
    types=models.CharField(max_length=50,null=True,blank=True)
    asset_id=models.CharField(max_length=50,null=True,blank=True)
    folder=models.CharField(max_length=50,null=True,blank=True)
    created_at=models.CharField(max_length=50,null=True,blank=True)
    signature=models.CharField(max_length=50,null=True,blank=True)
    version_id=models.CharField(max_length=50,null=True,blank=True)
    version=models.CharField(max_length=50,null=True,blank=True)

    def __str__(self) -> str:
        return self.user.full_name