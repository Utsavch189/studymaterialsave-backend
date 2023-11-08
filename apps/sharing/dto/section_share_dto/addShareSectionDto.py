from pydantic import BaseModel,validator,constr
from apps.sections.models.section import Section
from apps.auths.models.user import User

class AddShareSectionDTO(BaseModel):
    user:constr(min_length=1,max_length=50,strip_whitespace=True) # take id
    section:constr(min_length=1,max_length=50,strip_whitespace=True) # take id

    @validator('user',allow_reuse=True,always=True)
    def validate_user(cls,value):
        try:
            if User.objects.filter(username=value).exists():
                return User.objects.get(username=value)
            else:
                raise Exception('user not found!')
        except Exception as e:
            raise Exception(str(e))
    
    @validator('section',allow_reuse=True,always=True)
    def validate_section(cls,value):
        try:
            if Section.objects.filter(section_id=value).exists():
                return Section.objects.get(section_id=value)
            else:
                raise Exception('section not found!')
        except Exception as e:
            raise Exception(str(e))
