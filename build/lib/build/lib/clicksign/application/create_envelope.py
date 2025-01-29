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
    name: Optional[str] = None
    locale: Optional[str] = None
    auto_close: Optional[str] = None
    remind_interval: Optional[str] = None
    block_after_refusal: Optional[str] = None
    deadline_at: Optional[str] = None


@dataclass
class Output:
    id: UUID | None
    errors: list[str] = field(default_factory=list)


class CreateEnvelope:
    def __init__(self, envelope_adapter: IEnvelopeAdapter) -> None:
        self._envelope_adapter = envelope_adapter
        self._errors: list[str] = []

    async def execute(self, input: Input) -> Output:
        envelope = Envelope.create(
            type=input.type,
            name=input.name,
            locale=input.locale,
            auto_close=input.auto_close,
            remind_interval=input.remind_interval,
            block_after_refusal=input.block_after_refusal,
            deadline_at=input.deadline_at,
        )
        response = await self._envelope_adapter.create_envelope(envelope)
        if response.errors:
            return Output(id=None, errors=response.errors)
        return Output(id=envelope.id)
