from apps.sections.models.section import Section
from rest_framework import status
from apps.sections.dto.modifySection.main import ModifySectionDTO
from apps.sections.serializers.sectionReturnData.main import SectionReturnRespSerializer

class ModifySectionService:

    def modify(self,id:str,dto:ModifySectionDTO)->tuple:
        try:
            if not id:
                return ({"message":"section_id is needed!"},status.HTTP_406_NOT_ACCEPTABLE)
            
            if Section.objects.filter(section_id=id).exists():
                section=Section.objects.get(section_id=id)
                section.section_name=dto.section_name
                section.section_about=dto.section_about
                _data=SectionReturnRespSerializer(section).data
                section.save()
                return ({"section":_data,"message":"modified!"},status.HTTP_202_ACCEPTED)
            
            return ({"message":"not found!"},status.HTTP_404_NOT_FOUND)
        except Exception as e:
            raise Exception(str(e))