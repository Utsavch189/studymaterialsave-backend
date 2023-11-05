from dataclasses import dataclass,field
from datetime import datetime

@dataclass
class AllSections:
    section_id:str=field(default_factory=str)
    section_name:str=field(default_factory=str)
    section_about:str=field(default_factory=str)
    visibility:str=field(default_factory=str)
    created_at:datetime=field(default_factory=datetime)