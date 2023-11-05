from dataclasses import dataclass,field
from datetime import datetime
from typing import List

@dataclass
class PostMetaData:
    post_file_meta_id:str=field(default_factory=str)
    file_name:str=field(default_factory=str)
    file_url:str=field(default_factory=str)
    public_id:str=field(default_factory=str)
    resource_type:str=field(default_factory=str)
    types:str=field(default_factory=str)

@dataclass
class PostData:
    post_id:str=field(default_factory=str)
    title:str=field(default_factory=str)
    about:str=field(default_factory=str)
    notes:str=field(default_factory=str)
    visibility:str=field(default_factory=str)
    created_at:datetime=field(default_factory=datetime)
    post_meta:List[PostMetaData]=field(default_factory=list)