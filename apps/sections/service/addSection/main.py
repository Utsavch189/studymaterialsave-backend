from apps.sections.models.section import Section
from apps.sections.dto.addSection.main import AddSectionDTO
import uuid
from django.utils import timezone
from rest_framework import status
from apps.sections.serializers.sectionReturnData.main import SectionReturnRespSerializer

class AddSectionService:

    def add(self,dto:AddSectionDTO,request:object)->tuple:
        try:
            _user=request.User
            _section=Section(
                user=_user,
                section_id=uuid.uuid1(),
                section_name=dto.section_name,
                section_about=dto.section_about,
                created_at=timezone.now()
            )
            _section.save()
            return ({"message":"section is created!","data":SectionReturnRespSerializer(_section).data},status.HTTP_201_CREATED)
        except Exception as e:
            raise Exception(str(e))