from pydantic import BaseModel,validator,constr
from apps.sections.models.section import Section

class GetSectionDTO(BaseModel):
    section_id:constr(min_length=1,max_length=50,strip_whitespace=True)="None"

    @validator('section_id',allow_reuse=True,always=True)
    def validate_id(cls,value):
        try:
            if value!="None":
                if Section.objects.filter(section_id=value).exists():
                    return value
                else:
                    raise Exception("section is not found!")
            return None
        except Exception as e:
            raise Exception(str(e))
