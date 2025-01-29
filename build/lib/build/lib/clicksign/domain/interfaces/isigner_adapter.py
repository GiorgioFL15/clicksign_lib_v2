from uuid import UUID

from .isigner import ISigner


class ISignerAdapter:
    async def create_signer(self, signer: ISigner) -> None: ...
