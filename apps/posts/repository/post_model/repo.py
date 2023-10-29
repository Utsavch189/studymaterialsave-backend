from django.db import models
from typing import List
from apps.posts.dataContainers.main import PostData, PostMetaData
from .irepo import I_PostModelRepo


class PostModelRepo(models.Manager,I_PostModelRepo):

    def __init__(self) -> None:
        from django.db import connection
        self.conn=connection
    
    def getAllPostsOfASection(self, section_id: str) -> List[PostData]:
        try:
            res:List[PostData]=[]
            with self.conn.cursor() as c:
                c.execute("""SELECT post.post_id,post.title,post.about,post.notes,post.created_at,
                          postmeta.post_file_meta_id,postmeta.file_name,postmeta.file_url,postmeta.public_id,postmeta.resource_type,postmeta.types
                          FROM posts_post as post 

                          LEFT JOIN posts_postfilemeta as postmeta
                            ON postmeta.post_id=post.post_id
                          
                          INNER JOIN sections_section as section
                          ON post.section_id=section.section_id

                          WHERE section.section_id=%s
                          """,(section_id,)) # parameterized query
                for row in c.fetchall():
                    _postdata=PostData(
                        post_id=row[0],
                        title=row[1],
                        about=row[2],
                        notes=row[3],
                        created_at=row[4],
                    )
                    if row[5]!=None:
                        _postdata.post_meta.append(
                            PostMetaData(
                                post_file_meta_id=row[5],
                                file_name=row[6],
                                file_url=row[7],
                                public_id=row[8],
                                resource_type=row[9],
                                types=row[10]
                            )
                        )
                    res.append(_postdata)
            return res
        except Exception as e:
            raise Exception(str(e))
    
    def getAllPostMetaOfAPost(self, post_id: str) -> List[PostMetaData]:
        return super().getAllPostMetaOfAPost(post_id)