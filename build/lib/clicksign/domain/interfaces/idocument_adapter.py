from uuid import UUID

from .idocument import IDocument


class IDocumentAdapter:
    async def create_document(self, document: IDocument) -> None: ...
