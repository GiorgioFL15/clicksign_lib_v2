from dataclasses import dataclass
from typing import Optional
from uuid import UUID

from uuid_extensions import uuid7


@dataclass
class EnvelopeAdapterFakeResponse:
    id: UUID
    type: str
    name: str
    status: str
    errors: Optional[list[str]] = None


class FakeEnvelopeAdapter:
    async def create_envelope(self, envelope):
        if not envelope.name:
            return EnvelopeAdapterFakeResponse(
                id=uuid7(),
                type=envelope.type,
                name="",
                status="",
                errors=["Nome do envelope inválido"],
            )
        else:
            return EnvelopeAdapterFakeResponse(
                id=uuid7(),
                type=envelope.type,
                name=envelope.name,
                status="running",
            )

    async def activate_envelope(self, envelope):
        if envelope.status != "running":
            return EnvelopeAdapterFakeResponse(
                id=envelope.id,
                type=envelope.type,
                name=envelope.name,
                status=envelope.status,
                errors=["Envelope não pode ser ativado"],
            )
        else:
            return EnvelopeAdapterFakeResponse(
                id=envelope.id,
                type=envelope.type,
                name=envelope.name,
                status=envelope.status,
            )
