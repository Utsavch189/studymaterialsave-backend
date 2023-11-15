from core.utils.responses.response import Response
from rest_framework.views import APIView
from apps.users.dto.getUserDto.main import GetAUserDTO
from apps.users.service.getUserService.getAUser import GetAUserService
from core.utils.decorators.handelException import handel_exception
from core.utils.decorators.logger import log

import logging

logger=logging.getLogger('mylogger')

class GetAUser(APIView):
    
    @handel_exception
    @log(logger=logger)
    def get(self,request)->Response:
        _dto=GetAUserDTO(**request.data)
        message,status=GetAUserService(_dto).get(request)
        return Response(message,status=status,request=request)