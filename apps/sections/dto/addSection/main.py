from pydantic import BaseModel,validator,constr

class AddSectionDTO(BaseModel):
    section_name:constr(min_length=1,max_length=100,strip_whitespace=True)
    section_about:constr(min_length=1,max_length=150,strip_whitespace=True)=None