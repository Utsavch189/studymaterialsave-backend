from abc import ABC,abstractmethod
from apps.posts.dataContainers.main import PostData,PostMetaData
from typing import List

class I_PostModelRepo(ABC):

    @abstractmethod
    def getAPost(self,post_id:str)->PostData:
        pass

    @abstractmethod
    def getAllPostsOfASection(self,section_id:str)->List[PostData]:
        pass