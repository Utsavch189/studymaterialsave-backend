from abc import ABC,abstractmethod
from apps.users.serializers.getAllSharesSerializer.main import SharedSectionDataSerializer
from typing import List

class I_GetAllSharedSectionRepo(ABC):

    @abstractmethod
    def get_allSections(self,user_id:str)->List[SharedSectionDataSerializer]:
        pass