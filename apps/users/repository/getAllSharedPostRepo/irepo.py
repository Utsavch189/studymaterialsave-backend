from abc import ABC,abstractmethod
from apps.users.dataContainers.getAllSharesDataContainers.main import SharedPostDataContainer

from typing import List

class  I_GetAllSharedPostRepo(ABC):

    @abstractmethod
    def get_allPosts(self,user_id:str)->List[SharedPostDataContainer]: 
        pass