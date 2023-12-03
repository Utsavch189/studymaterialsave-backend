from apps.posts.models.post import Post
from apps.posts.models.post_file_meta import PostFileMeta
from django.db import transaction
from apps.posts.dto.addPost.main import AddPostDTO
from apps.sections.models.section import Section
import uuid
from django.utils import timezone
from core.utils.cdn.main import CDN
import concurrent.futures
from rest_framework import status
from apps.posts.serializers.getPosts import PostSerializer
from apps.posts.dataContainers.main import PostData, PostMetaData
import json

class AddPostService:

    def __init__(self,dto:AddPostDTO) -> None:
        self._dto=dto
        self._cdn=CDN()

    def _create_post(self)->Post:
        try:
            _section=Section.objects.get(section_id=self._dto.section_id)
            _post=Post(
                section=_section,
                post_id=uuid.uuid1(),
                title=self._dto.title,
                about=self._dto.about,
                notes=self._dto.notes,
                visibility=self._dto.visibility,
                created_at=timezone.now()
            )
            return _post
        except Exception as e:
            raise Exception(str(e))
    
    def _create_postFileMeta(self,result:dict,post:Post,file_name:str)->PostFileMeta:
        try:
            _postmeta=PostFileMeta(
                post=post,
                post_file_meta_id=uuid.uuid1(),
                file_name=file_name,
                file_url=result['secure_url'],
                public_id=result['public_id'],
                resource_type=result['resource_type'],
                types=result['type'],
                asset_id=result['asset_id'],
                folder=result['folder'],
                created_at=result['created_at'],
                signature=result['signature'],
                version_id=result['version_id'],
                version=result['version']
            )
            return _postmeta
        except Exception as e:
            raise Exception(str(e))
    
    def _upload_files(self,file_dict:dict)->tuple:
        try:
            _filename=file_dict['file_name'].split(".")[0]
            _res=self._cdn.upload(
                source=file_dict['file_b64'],
                destination=f"mynewapp/post/{_filename}"
            )
            return (_res,file_dict['file_name'])
        except Exception as e:
            raise Exception(str(e))


    @transaction.atomic
    def add(self)->tuple:
        try:
            
            with concurrent.futures.ThreadPoolExecutor() as executor:
                _files=self._dto.files
                _post=self._create_post()

                _post_dataContainer=PostData(
                    post_id=_post.post_id,
                    title=_post.title,
                    about=_post.about,
                    notes=_post.notes,
                    visibility=_post.visibility,
                    created_at=_post.created_at
                )

                if self._dto.files:
                    _uploads=executor.map(self._upload_files,_files)
                    executor.submit(_post.save())
                    for upload in _uploads:
                        _postMeta=self._create_postFileMeta(
                            upload[0],
                            _post,
                            upload[1]
                        )
                        _postMeta.save()
                        _postmeta_dataContainer=PostMetaData(
                            post_file_meta_id=_postMeta.post_file_meta_id,
                            file_name=_postMeta.file_name,
                            file_url=_postMeta.file_url,
                            public_id=_postMeta.public_id,
                            resource_type=_postMeta.resource_type,
                            types=_postMeta.types
                        )
                        _post_dataContainer.post_meta.append(_postmeta_dataContainer)
                _post.save()

                return (
                    {"message":"successfully created!","post":json.loads(json.dumps(PostSerializer(_post_dataContainer).data))},
                    status.HTTP_201_CREATED
                )

        except Exception as e:
            raise Exception(str(e))