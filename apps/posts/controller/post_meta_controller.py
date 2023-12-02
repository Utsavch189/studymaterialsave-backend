from core.utils.responses.response import Response
from rest_framework.views import APIView
from core.utils.decorators.handelException import handel_exception
from core.utils.decorators.logger import log
import logging
from apps.posts.dto.postMeta.deletePostMeta import DeletePostMetaDTO
from apps.posts.service.postMeta.deletePostMeta import DeletePostMetaService

logger=logging.getLogger('mylogger')

class PostMetaController(APIView):

    @handel_exception
    @log(logger=logger)
    def delete(self,request):
        _dto=DeletePostMetaDTO(**request.data)
        message,status=DeletePostMetaService(_dto).delete()
        print(message)
        return Response(message,status=status,request=request)
    
