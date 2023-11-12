from apps.sharing.models.sharedPosts import SharedPost
from apps.sharing.models.sharedSections import SharedSection
from rest_framework import status


class GetAllSharesService:

    def _getAllSharedPosts(self,user_id:str):
        pass

    def _getAllSharedSections(self,user_id:str):
        return SharedSection.repo().get_allSections(user_id)

    def get(self,request:object):
        try:
            _user=request.User
            
            _data=self._getAllSharedSections(_user.username)


            if len(_data)==0:
                _resp=({"message":"no shared sections!","data":_data},status.HTTP_200_OK)
            else:
                _resp=({"message":"fetched all shared sections!","data":_data},status.HTTP_204_NO_CONTENT)
            print(_resp)
            
            return _resp
        except Exception as e:
            raise Exception(str(e))