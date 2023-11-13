from abc import ABC,abstractmethod
from apps.users.dataContainers.getAllSharesDataContainers.main import SharedSectionDataContainer
from typing import List

class I_GetAllSharedSectionRepo(ABC):

    @abstractmethod
    def get_allSections(self,user_id:str)->List[SharedSectionDataContainer]:
        pass