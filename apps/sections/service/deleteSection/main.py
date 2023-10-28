from apps.sections.models.section import Section
from rest_framework import status

class DeleteSectionService:

    def delete(self,id:str)->tuple:
        try:
            if not id:
                return ({"message":"section_id is needed!"},status.HTTP_406_NOT_ACCEPTABLE)
            
            if Section.objects.filter(section_id=id).exists():
                Section.objects.get(section_id=id).delete()
                return ({"message":"deleted!"},status.HTTP_202_ACCEPTED)
            
            return ({"message":"not found!"},status.HTTP_404_NOT_FOUND)
        except Exception as e:
            raise Exception(str(e))