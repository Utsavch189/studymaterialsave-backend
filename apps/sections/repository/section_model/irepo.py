from abc import ABC,abstractstaticmethod
from apps.sections.repo_dataContainers.main import AllSections

class I_SectionModelRepo(ABC):

    @abstractstaticmethod
    def get_allSections(self,user_id:str)->list[AllSections]:
        pass