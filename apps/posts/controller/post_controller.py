from core.utils.responses.response import Response
from rest_framework.views import APIView
from core.utils.decorators.handelException import handel_exception
from core.utils.decorators.logger import log
import logging

from apps.posts.dto.addPost.main import AddPostDTO
from apps.posts.dto.getPost.main import GetPostDTO
from apps.posts.dto.deletePost.main import DeletePostDTO
from apps.posts.dto.modifyPost.main import ModifyPostDTO

from apps.posts.service.addPost.main import AddPostService
from apps.posts.service.getPost.main import GetPostService
from apps.posts.service.deletePost.main import DeletePostService
from apps.posts.service.modifyPost.main import ModifyPostService

logger=logging.getLogger('mylogger')

class PostGetController(APIView):
    @handel_exception
    @log(logger=logger)
    def get(self,request,section_id,post_id):
        print(section_id,post_id)
        _dto=GetPostDTO(**{
            "section_id":section_id,
            "post_id":post_id
        })
        message,status=GetPostService(_dto).get()
        return Response(message,status=status,request=request)

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
        _dto=ModifyPostDTO(**request.data)
        message,status=ModifyPostService(_dto).modify(request)
        return Response(message,status=status,request=request)

    @handel_exception
    @log(logger=logger)
    def delete(self,request):
        _dto=DeletePostDTO(**request.data)
        message,status=DeletePostService(_dto).delete(request)
        return Response(message,status=status,request=request)