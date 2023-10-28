from core.utils.responses.response import Response
from rest_framework.views import APIView
from apps.auths.dto.register.main_dto import RegisterMainDTO
from apps.auths.services.register.register_service import RegisterMainService
from core.utils.decorators.handelException import handel_exception
from core.utils.decorators.logger import log

import logging

logger=logging.getLogger('mylogger')

class Register(APIView):
    
    @handel_exception
    @log(logger=logger)
    def post(self,request)->Response:
        _dto=RegisterMainDTO(**request.data)
        data,status_code=RegisterMainService(dto=_dto).create()
        _login={
            "login":True,
            "sub":_dto.username
        }
        request.META={**request.META,**_login}
        return Response(data=data,status=status_code,request=request)