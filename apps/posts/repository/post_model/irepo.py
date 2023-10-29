from abc import ABC,abstractmethod
from apps.posts.dataContainers.main import PostData,PostMetaData
from typing import List

class I_PostModelRepo(ABC):

    @abstractmethod
    def getAllPostMetaOfAPost(self,post_id:str)->List[PostMetaData]:
        pass

    @abstractmethod
    def getAllPostsOfASection(self,section_id:str)->List[PostData]:
        pass