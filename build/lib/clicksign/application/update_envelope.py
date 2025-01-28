import re
from dataclasses import dataclass, field
from typing import Optional
from uuid import UUID

from clicksign.domain.envelope import Envelope
from clicksign.domain.interfaces.ienvelope_adapter import IEnvelopeAdapter


@dataclass
class Input:
    """Represents the input data for sign document process."""

    type: str
    status: str


@dataclass
class Output:
    id: UUID | None
    errors: list[str] = field(default_factory=list)


class UpdateEnvelope:
    def __init__(self, envelope_adapter: IEnvelopeAdapter) -> None:
        self._envelope_adapter = envelope_adapter
        self._errors: list[str] = []

    async def execute(self, input: Input) -> Output:
        envelope = Envelope.update(type=input.type, status=input.status)
        response = await self._envelope_adapter.activate_envelope(envelope)
        if response.errors:
            return Output(id=None, errors=response.errors)
        return Output(id=envelope.id)
