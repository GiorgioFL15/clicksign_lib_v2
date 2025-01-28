from typing import Protocol, Optional, Dict
from uuid import UUID


class IDocument(Protocol):
    @staticmethod
    def create(
        type: str,
        filename: str,
        content_base64: str,
        envelope_id: str,
        metadata: Optional[Dict] = None
    ) -> "IDocument": ...
    @property
    def id(self) -> UUID: ...
