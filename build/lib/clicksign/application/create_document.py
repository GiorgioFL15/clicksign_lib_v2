import re
from dataclasses import dataclass, field
from typing import Dict, Optional
from uuid import UUID

from clicksign.domain.document import Document
from clicksign.domain.interfaces.idocument_adapter import IDocumentAdapter


@dataclass
class Input:
    """Represents the input data for sign document process."""

    type: str
    filename: str
    content_base64: str
    envelope_id: str
    metadata: Optional[Dict] = None


@dataclass
class Output:
    id: UUID | None
    errors: list[str] = field(default_factory=list)


class CreateDocument:
    def __init__(self, document_adapter: IDocumentAdapter) -> None:
        self._document_adapter = document_adapter
        self._errors: list[str] = []

    async def execute(self, input: Input) -> Output:
        document = Document.create(
            type=input.type,
            filename=input.filename,
            content_base64=input.content_base64,
            envelope_id=input.envelope_id,
            metadata=input.metadata,
        )
        response = await self._document_adapter.create_document(document)
        if response.errors:
            return Output(id=None, errors=response.errors)
        return Output(id=document.id)
