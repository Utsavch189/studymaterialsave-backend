from core.utils.responses.response import Response
from rest_framework.views import APIView
from core.utils.decorators.handelException import handel_exception
from core.utils.decorators.logger import log
import logging
from apps.sharing.dto.section_share_dto.addShareDto import AddShareDTO
from apps.sharing.service.section_share_service.addShareService import AddShareService

logger=logging.getLogger('mylogger')

class SectionShareController(APIView):

    @handel_exception
    @log(logger=logger)
    def post(self,request):
        _dto=AddShareDTO(**request.data)
        message,status=AddShareService(_dto).add(request)
        return Response(message,status=status,request=request)