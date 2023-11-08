from apps.sections.models.section import Section
from rest_framework import status
from apps.sections.dto.deleteSection.main import DeleteSectionDTO

class DeleteSectionService:

    def delete(self,dto:DeleteSectionDTO,request:object)->tuple:
        try:
            _section=dto.section_id
            if request.User.username != _section.user.username:
                raise Exception("you can't delete this!")
            _section.delete()
            return ({"message":"deleted!"},status.HTTP_202_ACCEPTED) 
        except Exception as e:
            raise Exception(str(e))