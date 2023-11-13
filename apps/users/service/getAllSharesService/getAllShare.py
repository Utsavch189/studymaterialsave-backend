from apps.sharing.models.sharedPosts import SharedPost
from apps.sharing.models.sharedSections import SharedSection
from rest_framework import status
from apps.users.serializers.getAllSharesSerializer.main import SharedSectionDataSerializer
from apps.users.serializers.getAllSharesSerializer.main import SharedPostDataSerializer
import json

class GetAllSharesService:

    def _getAllSharedPosts(self,user_id:str):
        return SharedPost.repo().get_allPosts(user_id)

    def _getAllSharedSections(self,user_id:str):
        return SharedSection.repo().get_allSections(user_id)

    def get(self,request:object)->tuple:
        try:
            _user=request.User
            
            _sections=json.loads(json.dumps(SharedSectionDataSerializer(self._getAllSharedSections(_user.username),many=True).data))
            
            _posts=json.loads(json.dumps(SharedPostDataSerializer(self._getAllSharedPosts(_user.username),many=True).data))

            _resp=({"post":_posts,"sections":_sections},status.HTTP_200_OK)
            
            return _resp
        except Exception as e:
            raise Exception(str(e))