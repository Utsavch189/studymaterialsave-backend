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
            track:dict={}
            with self.conn.cursor() as c:
                c.execute("""SELECT post.post_id,post.title,post.about,post.notes,post.visibility,post.created_at,
                          postmeta.post_file_meta_id,postmeta.file_name,postmeta.file_url,postmeta.public_id,postmeta.resource_type,postmeta.types
                          FROM posts_post as post 

                          LEFT JOIN posts_postfilemeta as postmeta
                            ON postmeta.post_id=post.post_id
                          
                          INNER JOIN sections_section as section
                          ON post.section_id=section.section_id

                          WHERE section.section_id=%s
                          """,(section_id,)) # parameterized query
                for row in c.fetchall():
                    
                    if track.get(row[0]):
                        _postdata=track.get(row[0])
                    else:
                        _postdata=PostData(
                            post_id=row[0],
                            title=row[1],
                            about=row[2],
                            notes=row[3],
                            visibility=row[4],
                            created_at=row[5],
                        )
                        track[row[0]]=_postdata
                        res.append(_postdata)

                    if row[5]!=None:
                        _postdata.post_meta.append(
                            PostMetaData(
                                post_file_meta_id=row[6],
                                file_name=row[7],
                                file_url=row[8],
                                public_id=row[9],
                                resource_type=row[10],
                                types=row[11]
                            )
                        )
                    
            return res
        except Exception as e:
            raise Exception(str(e))
    
    def getAPost(self, post_id: str) -> PostData:
        try:
            track:dict={}
            with self.conn.cursor() as c:
                c.execute("""SELECT post.post_id,post.title,post.about,post.notes,post.visibility,post.created_at,
                          postmeta.post_file_meta_id,postmeta.file_name,postmeta.file_url,postmeta.public_id,postmeta.resource_type,postmeta.types
                          FROM posts_post as post 

                          LEFT JOIN posts_postfilemeta as postmeta
                            ON postmeta.post_id=post.post_id
                          
                          WHERE post.post_id=%s
                          """,(post_id,)) # parameterized query
                for row in c.fetchall():
 
                    if track.get(row[0]):
                        _postdata=track.get(row[0])
                    else:
                        _postdata=PostData(
                            post_id=row[0],
                            title=row[1],
                            about=row[2],
                            notes=row[3],
                            visibility=row[4],
                            created_at=row[5],
                        )
                        track[row[0]]=_postdata

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
                    
            return _postdata
        except Exception as e:
            raise Exception(str(e))