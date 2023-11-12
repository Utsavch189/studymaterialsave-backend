from dataclasses import dataclass,field
from datetime import datetime
from apps.sections.dataContainers.main import AllSections


@dataclass
class UserMeta:
    meta_id:str=field(default_factory=str)
    profile_pic_url:str=field(default_factory=str)
    doj:datetime=field(default_factory=str)

@dataclass
class UserData:
    user_id:str=field(default_factory=str)
    full_name:str=field(default_factory=str)
    email:str=field(default_factory=str)
    phone:str=field(default_factory=str)
    user_meta:UserMeta=field(default_factory=object)

@dataclass
class SharedSectionDataContainer:
    share_id:str=field(default_factory=str)
    from_user:UserData=field(default_factory=object)
    section:AllSections=field(default_factory=object)
    shared_at:datetime=field(default_factory=datetime)


@dataclass
class SharedPostDataContainer:
    share_id:str=field(default_factory=str)
    from_user=None
    post=None
    shared_at:datetime=field(default_factory=datetime)
