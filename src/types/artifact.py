# Models an artifact

from dataclasses import dataclass
from datetime import datetime

@dataclass
class Artifact:
    source: str
    artifact_type: str
    content: str
    timestamp: datetime
    url: str
    relevance_score: float = None