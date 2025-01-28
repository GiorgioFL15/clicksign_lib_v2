from dataclasses import dataclass, field
from typing import Optional
from uuid import UUID

from clicksign.domain.interfaces.isigner_adapter import ISignerAdapter
from clicksign.domain.signer import Signer


@dataclass
class Input:
    """Represents the input data for sign document process."""

    type: str
    envelope_id: str
    name: Optional[str] = None
    birthday: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    has_documentation: Optional[str] = None
    documentation: Optional[str] = None
    refusable: Optional[str] = None
    group: Optional[str] = None


@dataclass
class Output:
    id: UUID | None
    errors: list[str] = field(default_factory=list)


class CreateSigner:
    def __init__(self, signer_adapter: ISignerAdapter) -> None:
        self._signer_adapter = signer_adapter
        self._errors: list[str] = []

    async def execute(self, input: Input) -> Output:
        signer = Signer.create(
            type=input.type,
            envelope_id=input.envelope_id,
            name=input.name,
            birthday=input.birthday,
            email=input.email,
            phone_number=input.phone_number,
            has_documentation=input.has_documentation,
            documentation=input.documentation,
            refusable=input.refusable,
            group=input.group,
        )
        response = await self._signer_adapter.create_signer(signer)
        if response.errors:
            return Output(id=None, errors=response.errors)
        return Output(id=signer.id)
