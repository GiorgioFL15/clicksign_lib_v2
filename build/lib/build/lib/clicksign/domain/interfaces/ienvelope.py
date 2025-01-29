from typing import Optional, Protocol
from uuid import UUID


class IEnvelope(Protocol):
    @staticmethod
    def create(
        type: str,
        name: Optional[str] = None,
        locale: Optional[str] = None,
        auto_close: Optional[str] = None,
        remind_interval: Optional[str] = None,
        block_after_refusal: Optional[str] = None,
        deadline_at: Optional[str] = None,
    ) -> "IEnvelope": ...

    @staticmethod
    def update(
        type: str,
        status: Optional[str] = None,
    ) -> "IEnvelope": ...

    @property
    def id(self) -> UUID: ...
