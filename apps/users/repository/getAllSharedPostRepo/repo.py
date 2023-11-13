from django.db import models
from apps.users.dataContainers.getAllSharesDataContainers.main import SharedPostDataContainer,UserData,UserMeta,PostData,PostMetaData
from apps.users.repository.getAllSharedPostRepo.irepo import I_GetAllSharedPostRepo
from typing import Dict,List

class  GetAllSharedPostRepo(I_GetAllSharedPostRepo,models.Manager):

    def __init__(self) -> None:
        from django.db import connection
        self.conn=connection
    
    def get_allPosts(self,user_id:str)->List[SharedPostDataContainer]:
        try:
            res:Dict[str,SharedPostDataContainer]={}

            with self.conn.cursor() as c:
                c.execute("""
                          Select shared_posts.share_id,
                          shared_posts.from_user_id,from_user.full_name,from_user.email,from_user.phone,
                          from_user_meta.meta_id,from_user_meta.profile_pic_url,from_user_meta.doj,
                          shared_posts.post_id,post.title,post.about,post.notes,post.visibility,post.created_at,
                          post_meta.post_file_meta_id,post_meta.file_name,post_meta.file_url,post_meta.public_id,post_meta.resource_type,post_meta.types,
                          shared_posts.shared_at

                          From sharing_sharedpost as shared_posts

                          Left Join auths_user as from_user
                            On from_user.username=shared_posts.from_user_id

                          Left Join auths_usermeta as from_user_meta
                            On from_user_meta.user_id=shared_posts.from_user_id
                          
                          Left Join posts_post as post
                            On post.post_id=shared_posts.post_id
                          
                          Left Join posts_postfilemeta as post_meta
                            On post_meta.post_id=shared_posts.post_id
                          
                          where shared_posts.user_id=%s
                          """,(user_id,))
                for row in c.fetchall():
                    if not res.get(row[8]):
                        _usermeta=UserMeta(
                            meta_id=row[5],profile_pic_url=row[6],doj=row[7]
                        )
                        _userdata=UserData(
                            user_id=row[1],full_name=row[2],email=row[3],phone=row[4],user_meta=_usermeta
                        )
                        _post=PostData(post_id=row[8],title=row[9],about=row[10],notes=row[11],visibility=row[12],created_at=row[13])
                        _postmeta=PostMetaData(post_file_meta_id=row[14],file_name=row[15],file_url=row[16],public_id=row[17],resource_type=row[18],types=row[19])
                    
                        _post.post_meta.append(_postmeta)
                        _data=SharedPostDataContainer(share_id=row[0],from_user=_userdata,post=_post,shared_at=row[20])
                        res[row[8]]=_data
                    else:
                        _post=res.get(row[8]).post
                        
                        _postmeta=PostMetaData(post_file_meta_id=row[14],file_name=row[15],file_url=row[16],public_id=row[17],resource_type=row[18],types=row[19])
                    
                        _post.post_meta.append(_postmeta)
                    
                        _data=SharedPostDataContainer(share_id=row[0],from_user=_userdata,post=_post,shared_at=row[20])
                        res[row[8]]=_data
                
            return list(res.values())
        except Exception as e:
            raise Exception(str(e))