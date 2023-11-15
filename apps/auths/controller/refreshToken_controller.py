from core.utils.responses.response import Response
from rest_framework.views import APIView
from rest_framework import status
from core.utils.decorators.handelException import handel_exception
from core.utils.decorators.logger import log

import logging

logger=logging.getLogger('mylogger')

class RefreshToken(APIView):
    
    @handel_exception
    @log(logger=logger)
    def post(self,request)->Response:
        _login={
            "login":True,
            "sub":request.User.username
        }
        request.META={**request.META,**_login}
        return Response({"message":"token replaced!"},status=status.HTTP_200_OK,request=request)