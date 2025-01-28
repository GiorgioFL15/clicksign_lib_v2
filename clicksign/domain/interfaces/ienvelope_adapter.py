from uuid import UUID

from .ienvelope import IEnvelope


class IEnvelopeAdapter:
    async def create_envelope(self, envelope: IEnvelope) -> None: ...
    async def activate_envelope(self, envelope: IEnvelope) -> None: ...
