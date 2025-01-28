from .irequired_auth import IRequiredAuth


class IRequiredAuthAdapter:
    async def create_bulk_auth(self, irequired_auth: IRequiredAuth) -> None: ...
