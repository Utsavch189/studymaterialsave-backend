from core.utils.responses.response import Response
from rest_framework.views import APIView
from apps.auths.dto.login.main_dto import LoginMainDTO
from core.utils.decorators.handelException import handel_exception
from core.utils.decorators.logger import log
from rest_framework import status

import logging

logger=logging.getLogger('mylogger')

class Login(APIView):
    
    @handel_exception
    @log(logger=logger)
    def post(self,request)->Response:
        _dto=LoginMainDTO(**request.data)
        _login={
            "login":True,
            "sub":_dto.username
        }
        request.META={**request.META,**_login}
        return Response(data={"message":"logged in!"},status=status.HTTP_200_OK,request=request)