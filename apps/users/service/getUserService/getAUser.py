from apps.auths.serializer.register.main import UserSerializer
from apps.users.dto.getUserDto.main import GetAUserDTO
from rest_framework import status

class GetAUserService:

    def __init__(self,dto:GetAUserDTO) -> None:
        self._dto=dto
    
    def get(self,request)->tuple:
        try:
            if self._dto.username:
                _user=self._dto.username
            else:
                _user=request.User
            
            _data=UserSerializer(_user).data

            return (
                {"message":"user is found!","data":_data},
                status.HTTP_200_OK
            )

        except Exception as e:
            raise Exception(str(e))
