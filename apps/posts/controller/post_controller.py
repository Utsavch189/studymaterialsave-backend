from core.utils.responses.response import Response
from rest_framework.views import APIView
from core.utils.decorators.handelException import handel_exception
from core.utils.decorators.logger import log
import logging
from apps.posts.dto.addPost.main import AddPostDTO
from apps.posts.dto.getPost.main import GetPostDTO
from apps.posts.service.addPost.main import AddPostService
from apps.posts.service.getPost.main import GetPostService

logger=logging.getLogger('mylogger')

class PostController(APIView):

    @handel_exception
    @log(logger=logger)
    def get(self,request):
        _dto=GetPostDTO(**request.data)
        message,status=GetPostService(_dto).get()
        return Response(message,status=status,request=request)

    @handel_exception
    @log(logger=logger)
    def post(self,request):
        _dto=AddPostDTO(**request.data)
        message,status=AddPostService(_dto).add()
        return Response(message,status=status,request=request)

    @handel_exception
    @log(logger=logger)
    def put(self,request):
        
        message,status={}
        return Response(message,status=status,request=request)

    @handel_exception
    @log(logger=logger)
    def delete(self,request):
        
        message,status={}
        return Response(message,status=status,request=request)