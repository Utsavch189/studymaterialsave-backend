from django.db import models
from django.contrib.auth.hashers import check_password

class User(models.Model):
    username=models.CharField(max_length=100,primary_key=True,default="")
    password=models.TextField()
    full_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    phone=models.CharField(max_length=10,unique=True)

    class Meta:
        indexes=[
            models.Index(fields=['phone','email'])
        ]

    def is_valid_password(self,password):
        return check_password(password,self.password)

    def __str__(self) -> str:
        return self.full_name