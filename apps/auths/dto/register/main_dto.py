from pydantic import BaseModel,validator,constr
import re
from ...models.user import User
from django.contrib.auth.hashers import make_password

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

class RegisterMainDTO(BaseModel):
    username:constr(min_length=1,max_length=100,strip_whitespace=True)
    confirm_password:constr(min_length=6,strip_whitespace=True,max_length=10)=None
    password:constr(min_length=6,max_length=10,strip_whitespace=True)
    full_name:constr(min_length=1,max_length=100,strip_whitespace=True)
    email:constr(min_length=1,max_length=100,strip_whitespace=True)
    phone:constr(min_length=1,max_length=10,strip_whitespace=True)
    profile_pic_name:constr(strip_whitespace=True)=None
    profile_pic_base64:constr(strip_whitespace=True)=None
    

    @validator('profile_pic_base64',allow_reuse=True,always=True)
    def profile_pic_base64(cls,value):
        if value:
            if len(value.split(','))>1:
                return value.split(',')[1]
            else:
                return value

    @validator('password',allow_reuse=True,always=True)
    def check_password(cls,value,values):
        try:
            if value and values['confirm_password']:
                confirm_password=values['confirm_password']
                if value==confirm_password:
                    return make_password(value)
                else:
                    raise ValueError("Passwords are not same")
            else:
                return make_password(value)
        except Exception as e:
            raise Exception(str(e))
    
    @validator('email',allow_reuse=True,always=True)
    def check_email(cls,value):
        try:
            if value:
                if re.fullmatch(email_regex,value):
                    if User.objects.filter(email=value).exists():
                        raise ValueError("email already exists!")
                    return value.lower()
                else:
                    raise ValueError("invalid email!")
        except Exception as e:
            raise Exception(str(e))
    
    @validator('username',allow_reuse=True,always=True)
    def check_username(cls,value):
        try:
            if value:
                if not User.objects.filter(username=value).exists():
                    return value
                else:
                    raise ValueError("user already exists!")
        except Exception as e:
            raise Exception(str(e))
    
    @validator('phone',allow_reuse=True,always=True)
    def check_phone(cls,value):
        try:
            if value:
                if not User.objects.filter(phone=value).exists():
                    return value
                else:
                    raise ValueError("phone number already exists!")
        except Exception as e:
            raise Exception(str(e))