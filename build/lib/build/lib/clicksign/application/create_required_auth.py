from dataclasses import dataclass, field
from typing import Optional
from uuid import UUID

from clicksign.domain.interfaces.irequired_auth_adapter import IRequiredAuthAdapter
from clicksign.domain.required_auth import RequiredAuth


@dataclass
class Input:
    type: str
    envelope_id: str
    first_opp: Optional[str] = None
    first_action: Optional[str] = None
    auth: Optional[str] = None
    second_opp: Optional[str] = None
    second_action: Optional[str] = None
    role: Optional[str] = None
    document_id: Optional[str] = None
    signer_id: Optional[str] = None


@dataclass
class Output:
    id: UUID | None
    errors: list[str] = field(default_factory=list)


class CreateRequiredAuth:
    def __init__(self, required_auth_adapter: IRequiredAuthAdapter) -> None:
        self._required_auth_adapter = required_auth_adapter
        self._errors: list[str] = []

    async def execute(self, input: Input) -> Output:
        required_auth = RequiredAuth.create(
            type=input.type,
            envelope_id=input.envelope_id,
            first_opp=input.first_opp,
            first_action=input.first_action,
            auth=input.auth,
            second_opp=input.second_opp,
            second_action=input.second_action,
            role=input.role,
            document_id=input.document_id,
            signer_id=input.signer_id,
        )
        response = await self._required_auth_adapter.create_bulk_auth(required_auth)
        if response.errors:
            return Output(id=None, errors=response.errors)
        return Output(id=required_auth.id)
