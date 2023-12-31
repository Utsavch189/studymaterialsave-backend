from django.db import models
from apps.sections.dataContainers.main import AllSections
from .irepo import I_SectionModelRepo

class SectionModelRepo(models.Manager,I_SectionModelRepo):

    def __init__(self) -> None:
        from django.db import connection
        self.conn=connection
        
    def get_allSections(self,user_id:str)->list[AllSections]:
        try:
            res:list[AllSections]=[]
            with self.conn.cursor() as c:
                c.execute("""select section.section_id,section.section_name,section.section_about,section.visibility,section.created_at from sections_section as section Join auths_user as user on user.username=section.user_id where user.username=%s""",(user_id,)) # parameterized query
                for row in c.fetchall():
                    data=AllSections(section_id=row[0],section_name=row[1],section_about=row[2],visibility=row[3],created_at=row[4])
                    res.append(data)
            return res
        except Exception as e:
            raise Exception(str(e))