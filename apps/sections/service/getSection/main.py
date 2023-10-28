from apps.sections.models.section import Section
from apps.sections.serializers.sectionReturnData.main import SectionReturnRespSerializer
from rest_framework import status
from apps.sections.repo_dataContainers.main import AllSections
import json
from apps.sections.dto.getSection.main import GetSectionDTO

class GetSectionService:

    def _getAllSections(self,request)->list[AllSections]:
        try:
            user_id=request.User.username
            return Section.repo().get_allSections(user_id=user_id)
        except Exception as e:
            raise Exception(str(e))
    
    def _getASection(self,id)->Section:
        try:
            return Section.objects.get(section_id=id)  
        except Exception as e:
            raise Exception(str(e))

    def get(self,request:object,dto:GetSectionDTO)->tuple:
        try:
            _id=dto.section_id
            if _id:
                _data=self._getASection(_id)
                _result=SectionReturnRespSerializer(_data).data
                
            else:
                _data=self._getAllSections(request)
                _result=json.loads(json.dumps(SectionReturnRespSerializer(_data,many=True).data))

            return ({"section":_result,"message":"successfully fetched!"},status.HTTP_200_OK)
        except Exception as e:
            raise Exception(str(e))
