from apps.auths.models.user import User
from apps.auths.models.usermeta import UserMeta
from apps.auths.models.profile_pic_meta import ProfilePicMeta
from apps.auths.dto.register.main_dto import RegisterMainDTO
from apps.auths.serializer.register.main import RegisterSerializer,RegisterUserMetaSerializer
from rest_framework import status
from django.utils import timezone
from django.db import transaction
import uuid
from core.utils.cdn.main import CDN
import concurrent.futures
from threading import Thread

class RegisterMainService:

    def __init__(self,dto:RegisterMainDTO) -> None:
        self._dto=dto
        self._cdn=CDN()

    def _create_user(self)->User:
        try:
            user=User(
                username=self._dto.username,
                password=self._dto.password,
                full_name=self._dto.full_name,
                email=self._dto.email,
                phone=self._dto.phone
            )
            return user
        except Exception as e:
            raise Exception(str(e))
    
    def _create_userMeta(self,_user:User,_result:dict)->UserMeta:
        try:
            usermeta=UserMeta(
                user=_user,
                meta_id=uuid.uuid3(namespace=uuid.NAMESPACE_DNS,name=self._dto.username),
                profile_pic_url=_result['secure_url'],
                doj=timezone.now()
            )
            return usermeta
        except Exception as e:
            raise Exception(str(e))
    
    def _create_profilePicMeta(self,_user:User,_result:dict)->ProfilePicMeta:
        try:
            profile_pic_meta=ProfilePicMeta(
                    user=_user,
                    profile_pic_meta_id=uuid.uuid3(namespace=uuid.NAMESPACE_DNS,name=self._dto.profile_pic_name),
                    picture_name=self._dto.profile_pic_name,
                    public_id=_result['public_id'],
                    resource_type=_result['resource_type'],
                    types=_result['type'],
                    asset_id=_result['asset_id'],
                    folder=_result['folder'],
                    created_at=_result['created_at'],
                    signature=_result['signature'],
                    version_id=_result['version_id'],
                    version=_result['version']
                )
            return profile_pic_meta
        except Exception as e:
            raise Exception(str(e))


    def _upload_pic(self):
        try:
            if self._dto.profile_pic_base64 and self._dto.profile_pic_name:
                _filename=self._dto.profile_pic_name.split(".")[0]
                _result=self._cdn.upload(
                    source=self._dto.profile_pic_base64,
                    destination=f"mynewapp/profile/{_filename}"
                )
                return _result,True
            return {'secure_url':""},False
        except Exception as e:
            raise Exception(str(e))

    @transaction.atomic
    def create(self)->tuple:
        try:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                _upload=self._upload_pic()
                _user=self._create_user()

                _result=_upload[0]
                _status=_upload[1]

                _usermeta=self._create_userMeta(_user,_result)

                if _status:
                    _profile_pic_meta=self._create_profilePicMeta(_user,_result)
                    executor.submit(_profile_pic_meta.save())

                executor.submit(_usermeta.save())
                executor.submit(_user.save())
    
            data={
                "message":"account is creatd!",
                "user":RegisterSerializer(_user).data,
                "usermeta":RegisterUserMetaSerializer(_usermeta).data
            }
            return (data,status.HTTP_201_CREATED)
        except Exception as e:
            t=Thread(target=self._cdn.delete,args=(_result['public_id'],
                _result['resource_type'],
                _result['type']))
            t.start()
            raise Exception(e)