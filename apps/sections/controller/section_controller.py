from core.utils.responses.response import Response
from rest_framework.views import APIView
from core.utils.decorators.handelException import handel_exception
from core.utils.decorators.logger import log
from apps.sections.dto.addSection.main import AddSectionDTO
from apps.sections.dto.modifySection.main import ModifySectionDTO
import logging
from apps.sections.service.addSection.main import AddSectionService
from apps.sections.service.getSection.main import GetSectionService
from apps.sections.service.deleteSection.main import DeleteSectionService
from apps.sections.service.modifySection.main import ModifySectionService

logger=logging.getLogger('mylogger')

class SectionController(APIView):

    @handel_exception
    @log(logger=logger)
    def get(self,request,id=None):
        message,status=GetSectionService().get(request,id)
        return Response(message,status=status)

    @handel_exception
    @log(logger=logger)
    def post(self,request,id=None):
        _dto=AddSectionDTO(**request.data)
        message,status=AddSectionService().add(_dto,request)
        return Response(message,status=status)

    @handel_exception
    @log(logger=logger)
    def put(self,request,id=None):
        _dto=ModifySectionDTO(**request.data)
        message,status=ModifySectionService().modify(id,_dto)
        return Response(message,status=status)

    @handel_exception
    @log(logger=logger)
    def delete(self,request,id=None):
        message,status=DeleteSectionService().delete(id)
        return Response(message,status=status)