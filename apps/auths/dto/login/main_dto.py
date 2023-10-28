from pydantic import BaseModel,validator,constr
from ...models.user import User

class LoginMainDTO(BaseModel):
    username:constr(min_length=1,max_length=100,strip_whitespace=True)
    password:constr(min_length=6,max_length=10,strip_whitespace=True)

    @validator('username',allow_reuse=True,always=True)
    def check_username(cls,value):
        try:
            if value and User.objects.filter(username=value).exists():
                return value
            else:
                raise ValueError("username doesn't exists")
                
        except Exception as e:
            raise Exception(str(e))

    @validator('password',allow_reuse=True,always=True)
    def check_password(cls,value,values):
        try:
            if value:
                user=User.objects.get(username=values['username'])
                if user.is_valid_password(value):
                    return value
                else:
                    raise ValueError("password is invalid!")
        except Exception as e:
            raise Exception(str(e))
        