from pydantic import BaseModel,validator,constr
from apps.sections.models.section import Section

VISIBILITY=['PUBLIC','PRIVATE']

class ModifySectionDTO(BaseModel):
    section_id:constr(min_length=1,max_length=50,strip_whitespace=True)
    section_name:constr(max_length=100,strip_whitespace=True)
    section_about:constr(max_length=150,strip_whitespace=True)
    visibility:constr(max_length=10,strip_whitespace=True)

    @validator('section_id',allow_reuse=True,always=True)
    def validate_id(cls,value):
        try:
            if value:
                if Section.objects.filter(section_id=value).exists():
                    return value
                else:
                    raise Exception("section is not found!")
        except Exception as e:
            raise Exception(str(e))
    
    @validator('visibility',allow_reuse=True,always=True)
    def visibility_validate(cls,value):
        if not value.upper() in VISIBILITY:
            raise Exception('visibility should be either public or private!')
        return value.upper()