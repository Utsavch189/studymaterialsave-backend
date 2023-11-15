from pydantic import BaseModel,validator,constr
from apps.auths.models.user import User

class GetAUserDTO(BaseModel):
    username:constr(max_length=100,strip_whitespace=True)=""

    @validator('username',allow_reuse=True,always=True)
    def validate_username(cls,value):
        try:
            if value:
                if User.objects.filter(username=value).exists():
                    return User.objects.get(username=value)
                raise Exception("username doesn't exists!")
            else:
                return None
        except Exception as e:
            raise Exception(str(e))