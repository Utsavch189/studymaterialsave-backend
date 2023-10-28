from apps.sections.models.section import Section
from rest_framework import status
from apps.sections.dto.deleteSection.main import DeleteSectionDTO

class DeleteSectionService:

    def delete(self,dto:DeleteSectionDTO)->tuple:
        try:
            Section.objects.get(section_id=dto.section_id).delete()
            return ({"message":"deleted!"},status.HTTP_202_ACCEPTED) 
        except Exception as e:
            raise Exception(str(e))