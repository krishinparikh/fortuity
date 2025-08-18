# Models a person

from dataclasses import dataclass
from .artifact import Artifact

@dataclass
class Person:
    name: str
    email: str
    phone: str
    company: str
    title: str
    associated_artifacts: list[Artifact]