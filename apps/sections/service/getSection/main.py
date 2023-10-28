from apps.sections.models.section import Section
from apps.sections.serializers.sectionReturnData.main import SectionReturnRespSerializer
from rest_framework import status
from apps.sections.repo_dataContainers.main import AllSections
import json

class GetSectionService:

    def _getAllSections(self,request)->list[AllSections]:
        try:
            user_id=request.User.username
            return Section.repo().get_allSections(user_id=user_id)
        except Exception as e:
            raise Exception(str(e))
    
    def _getASection(self,id)->Section:
        try:
            if Section.objects.filter(section_id=id).exists():
                return Section.objects.get(section_id=id)
            return None
        except Exception as e:
            raise Exception(str(e))

    def get(self,request:object,id:str)->tuple:
        try:
            if id:
                _data=self._getASection(id)
                if _data:
                    _result=SectionReturnRespSerializer(_data).data
                else:
                    return ({"message":"not found!"},status.HTTP_404_NOT_FOUND)
            else:
                _data=self._getAllSections(request)
                _result=json.loads(json.dumps(SectionReturnRespSerializer(_data,many=True).data))

            return ({"section":_result,"message":"successfully fetched!"},status.HTTP_200_OK)
        except Exception as e:
            raise Exception(str(e))
