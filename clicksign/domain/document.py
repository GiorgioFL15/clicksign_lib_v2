from uuid import UUID
from typing import Optional, Dict


class Document:
    def __init__(
        self,
        type: str,
        filename: str,
        content_base64: str,
        envelope_id: str,
        metadata: Optional[Dict] = None
    ):
        self._type = type
        self._filename = filename
        self._content_base64 = content_base64
        self._envelope_id = envelope_id
        self._metadata = metadata
        self._id = id
        self._signers: Dict[str, UUID] = {}

    @staticmethod
    def create(
        type: str,
        filename: Optional[str] = None,
        content_base64: Optional[str] = None,
        envelope_id: Optional[str] = None,
        metadata: Optional[Dict] = None,
    ) -> "Document":
        document = Document(
            type=type,
            filename=filename,
            content_base64=content_base64,
            envelope_id=envelope_id,
            metadata=metadata,
        )
        return document

    def get_errors(self) -> list[str]:
        return self._errors

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def type(self) -> str:
        return self._type

    @property
    def filename(self) -> str:
        return self._filename

    @property
    def content_base64(self) -> str:
        return self._content_base64

    @property
    def envelope_id(self) -> str:
        return self._envelope_id

    @property
    def metadata(self) -> Optional[Dict]:
        return self._metadata

    @property
    def signers(self) -> Dict[str, UUID]:
        return self._signers
