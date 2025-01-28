from typing import Protocol, Optional
from uuid import UUID


class IRequiredAuth(Protocol):
    @staticmethod
    def create(
        type: str,
        envelope_id: str,
        first_opp: Optional[str] = None,
        first_action: Optional[str] = None,
        auth: Optional[str] = None,
        second_opp: Optional[str] = None,
        second_action: Optional[str] = None,
        role: Optional[str] = None,
        document_id: Optional[str] = None,
        signer_id: Optional[str] = None,
    ) -> "IRequiredAuth": ...
    @property
    def id(self) -> UUID: ...
