from apps.sharing.models.sharedSections import SharedSection
from rest_framework import status
from apps.sharing.dto.section_share_dto.addShareSectionDto import AddShareSectionDTO
from django.utils import timezone
from apps.sharing.serializer.section_share_serializer.main import SharedSectionSerializer 
import uuid
from datetime import datetime

class AddShareSectionService:

    def __init__(self,dto:AddShareSectionDTO) -> None:
        self._dto=dto
    
    def add(self,request:object)->tuple:
        try:
            _user=request.User

            if not _user.username==self._dto.section.user.username:
                raise Exception("you can not share this!")
            
            _shared_section=SharedSection(
                share_id=uuid.uuid3(namespace=uuid.NAMESPACE_DNS,name=str(datetime.now())),
                user=self._dto.user,
                from_user=_user,
                section=self._dto.section,
                shared_at=timezone.now()
            )
            _shared_section.save()
            return (
                {"message":"successfully shared!","shared_data":SharedSectionSerializer(_shared_section).data},
                status.HTTP_202_ACCEPTED
            )

        except Exception as e:
            raise Exception(str(e))