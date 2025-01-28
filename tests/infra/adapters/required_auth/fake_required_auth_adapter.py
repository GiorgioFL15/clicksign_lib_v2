from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class RequiredAuthAdapterFakeResponse:
    id: str
    type: str
    attributes: Dict
    errors: Optional[list[str]] = None

class FakeRequiredAuthAdapter:
    async def create_bulk_auth(self, required_auth):
        if not required_auth.envelope_id:
            return RequiredAuthAdapterFakeResponse(
                id="",
                type="",
                attributes={},
                errors=["Envelope ID inválido"],
            )
        else:
            return RequiredAuthAdapterFakeResponse(
                id="fake-id",
                type="bulk_requirements",
                attributes={
                    "first_action": required_auth.first_action,
                    "first_auth": required_auth.auth,
                    "second_action": required_auth.second_action,
                    "second_role": required_auth.role,
                },
            )