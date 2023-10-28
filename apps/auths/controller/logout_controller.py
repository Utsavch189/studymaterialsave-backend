from core.utils.responses.response import Response
from rest_framework.views import APIView
from core.utils.decorators.handelException import handel_exception
from core.utils.decorators.logger import log
from rest_framework import status

import logging

logger=logging.getLogger('mylogger')

class Logout(APIView):
    
    @handel_exception
    @log(logger=logger)
    def post(self,request)->Response:
        _logout={
            "logout":True
        }
        request.META={**request.META,**_logout}
        return Response(data={"message":"logged out!"},status=status.HTTP_200_OK,request=request)