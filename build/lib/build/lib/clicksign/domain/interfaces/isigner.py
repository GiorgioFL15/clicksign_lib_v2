from typing import Dict, Optional, Protocol
from uuid import UUID


class ISigner(Protocol):
    @staticmethod
    def create(
        type: str,
        filename: str,
        content_base64: str,
        envelope_id: str,
        metadata: Optional[Dict] = None,
    ) -> "ISigner": ...
    @property
    def id(self) -> UUID: ...
