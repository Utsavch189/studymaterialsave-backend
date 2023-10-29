from pydantic import BaseModel,validator,constr,conlist
from apps.posts.models.post import Post
from apps.posts.models.post_file_meta import PostFileMeta
from apps.sections.models.section import Section

"""
files=[
    {"file_name":...,"file_b64":...,"file_type":...}
]
"""

class AddPostDTO(BaseModel):
    section_id:constr(min_length=1,max_length=50,strip_whitespace=True)
    title:constr(min_length=1,max_length=50,strip_whitespace=True)
    about:constr(min_length=1,max_length=150,strip_whitespace=True)
    files:conlist(dict,max_length=5)=[]
    notes:constr(min_length=1,strip_whitespace=True)=None

    @validator('title',allow_reuse=True,always=True)
    def title_validate(cls,value):
        try:
            if not Post.objects.filter(title=value).exists():
                return value
            else:
                raise Exception("already same title exists..")
        except Exception as e:
            raise Exception(str(e))
        
    @validator('files',allow_reuse=True,always=True)
    def file_validate(cls,value):
        try:
            if len(value)>0:
                for i in value:
                    if PostFileMeta.objects.filter(file_name=i['file_name']).exists():
                        raise Exception(f"{i['file_name']} already exists!")
                return value
            return []
        except Exception as e:
            raise Exception(str(e))
    
    @validator('section_id',allow_reuse=True,always=True)
    def validate_id(cls,value):
        try:
            if value!="None":
                if Section.objects.filter(section_id=value).exists():
                    return value
                else:
                    raise Exception("section_id is not valid!")
            return None
        except Exception as e:
            raise Exception(str(e))