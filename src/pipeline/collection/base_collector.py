# Abstract base class for collecting artifacts from a source
# Result is a list of Artifacts

from abc import ABC, abstractmethod
from typing import List
from src.types.artifact import Artifact

class BaseCollector(ABC):
    @abstractmethod
    def collect_artifacts(self) -> List[Artifact]:
        pass