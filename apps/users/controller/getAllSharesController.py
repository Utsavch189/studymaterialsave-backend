from core.utils.responses.response import Response
from rest_framework.views import APIView
from rest_framework import status
from core.utils.decorators.handelException import handel_exception
from core.utils.decorators.logger import log
import logging
from apps.users.service.getAllSharesService.getAllShare import GetAllSharesService

logger=logging.getLogger('mylogger')

class GetAllSharesController(APIView):

    @handel_exception
    @log(logger=logger)
    def get(self,request:object):
        message,status=GetAllSharesService().get(request)
        return Response(message,status)