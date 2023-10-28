from pydantic import BaseModel,validator,constr

class ModifySectionDTO(BaseModel):
    section_name:constr(max_length=100,strip_whitespace=True)
    section_about:constr(max_length=150,strip_whitespace=True)