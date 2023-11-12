from core.utils.responses.response import Response
from rest_framework.views import APIView
from rest_framework import status
from core.utils.decorators.handelException import handel_exception
from core.utils.decorators.logger import log
import logging
from apps.sharing.dto.post_share_dto.addSharePostDto import AddSharePostDTO
from apps.sharing.service.post_share_service.addShareService import AddSharePostService
from apps.sharing.dto.post_share_dto.deleteSharedPostDto import DeleteASharedPostDTO

logger=logging.getLogger('mylogger')

class PostShareController(APIView):

    @handel_exception
    @log(logger=logger)
    def post(self,request):
        _dto=AddSharePostDTO(**request.data)
        message,status=AddSharePostService(_dto).add(request)
        return Response(message,status=status,request=request)

    @handel_exception
    @log(logger=logger)
    def delete(self,request):
        _dto=DeleteASharedPostDTO(**request.data)
        _shared_post=_dto.share_id
        if request.User.username != _shared_post.section.user.username:
            raise Exception("you can't delete this!")
        _shared_post.delete()
        return Response({"message":"successfully deleted!"},status=status.HTTP_202_ACCEPTED,request=request)