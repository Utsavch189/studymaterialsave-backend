from core.utils.responses.response import Response
from rest_framework.views import APIView
from rest_framework import status
from core.utils.decorators.handelException import handel_exception
from core.utils.decorators.logger import log
import logging
from apps.sharing.dto.section_share_dto.addShareSectionDto import AddShareSectionDTO
from apps.sharing.dto.section_share_dto.deleteSharedSectionDto import DeleteASharedSectionDTO
from apps.sharing.service.section_share_service.addShareService import AddShareSectionService

logger=logging.getLogger('mylogger')

class SectionShareController(APIView):

    @handel_exception
    @log(logger=logger)
    def post(self,request):
        _dto=AddShareSectionDTO(**request.data)
        message,status=AddShareSectionService(_dto).add(request)
        return Response(message,status=status,request=request)

    @handel_exception
    @log(logger=logger)
    def delete(self,request):
        _dto=DeleteASharedSectionDTO(**request.data)
        _shared_section=_dto.share_id
        if request.User.username != _shared_section.to_user.username:
            raise Exception("you can't delete this!")
        _shared_section.delete()
        return Response({"message":"successfully deleted!"},status=status.HTTP_202_ACCEPTED,request=request)