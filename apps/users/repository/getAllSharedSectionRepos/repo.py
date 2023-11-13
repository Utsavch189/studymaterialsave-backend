from django.db import models
from apps.users.dataContainers.getAllSharesDataContainers.main import SharedSectionDataContainer,UserMeta,UserData
from typing import List
from apps.users.repository.getAllSharedSectionRepos.irepo import I_GetAllSharedSectionRepo
from apps.sections.dataContainers.main import AllSections


class  GetAllSharedSectionRepo(I_GetAllSharedSectionRepo,models.Manager):

    def __init__(self) -> None:
        from django.db import connection
        self.conn=connection
        
    def get_allSections(self, user_id: str) -> List[SharedSectionDataContainer]:
        try:
            res:List[SharedSectionDataContainer]=[]
            with self.conn.cursor() as c:
                c.execute("""
                            Select shared_sections.share_id,
                            shared_sections.from_user_id,from_user.full_name,from_user.email,from_user.phone,
                            from_user_meta.meta_id,from_user_meta.profile_pic_url,from_user_meta.doj,
                            shared_sections.section_id,section.section_name,section.section_about,section.visibility,section.created_at,
                            shared_sections.shared_at
                          
                            From sharing_sharedsection as shared_sections
                          
                            Left Join auths_user as from_user
                                On from_user.username=shared_sections.from_user_id

                            Left Join auths_usermeta as from_user_meta
                                On from_user_meta.user_id=shared_sections.from_user_id
                            
                            Left Join sections_section as section
                                On section.section_id=shared_sections.section_id
                          
                            where shared_sections.user_id=%s""",(user_id,)) # parameterized query
                for row in c.fetchall():
                    _usermeta=UserMeta(
                        meta_id=row[5],profile_pic_url=row[6],doj=row[7]
                    )
                    _userdata=UserData(
                        user_id=row[1],full_name=row[2],email=row[3],phone=row[4],user_meta=_usermeta
                    )
                    _section=AllSections(
                        section_id=row[8],section_name=row[9],section_about=row[10],visibility=row[11],created_at=row[12]
                    )

                    _sharedSectionData=SharedSectionDataContainer(
                        share_id=row[0],from_user=_userdata,section=_section,shared_at=row[13]
                    )
                    res.append(_sharedSectionData)
            return res 
        except Exception as e:
            raise Exception(str(e))
