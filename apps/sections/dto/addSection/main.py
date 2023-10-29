from pydantic import BaseModel,validator,constr
from apps.sections.models.section import Section

class AddSectionDTO(BaseModel):
    section_name:constr(min_length=1,max_length=100,strip_whitespace=True)
    section_about:constr(min_length=1,max_length=150,strip_whitespace=True)=None

    @validator('section_name',allow_reuse=True,always=True)
    def section_name_validate(cls,value):
        try:
            if value:
                if not Section.objects.filter(section_name=value).exists():
                    return value
                else:
                    raise Exception("section name already exists!")
        except Exception as e:
            raise Exception(str(e))