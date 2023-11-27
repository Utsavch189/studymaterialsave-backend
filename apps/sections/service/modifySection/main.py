from apps.sections.models.section import Section
from rest_framework import status
from apps.sections.dto.modifySection.main import ModifySectionDTO
from apps.sections.serializers.sectionReturnData.main import SectionReturnRespSerializer

class ModifySectionService:

    def modify(self,dto:ModifySectionDTO,request:object)->tuple:
        try:
            _section=dto.section_id
            print(_section)
            
            if request.User.username != _section.user.username:
                raise Exception("you can't modify this!")
        
            _section.section_name=dto.section_name
            _section.section_about=dto.section_about
            _section.visibility=dto.visibility
     
            _data=SectionReturnRespSerializer(_section).data
            
            _section.save()
            return ({"section":_data,"message":"modified!"},status.HTTP_202_ACCEPTED)
        
        except Exception as e:
            raise Exception(str(e))