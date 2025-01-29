from dataclasses import asdict

import httpx

from clicksign.domain.envelope import Envelope
from clicksign.domain.interfaces.ienvelope_adapter import IEnvelopeAdapter


class EnvelopeClicksignAdapter(IEnvelopeAdapter):
    def __init__(self, auth_token: str, base_url: str):
        self._auth_token = auth_token
        self._base_url = base_url

    async def create_envelope(self, envelope: Envelope) -> dict:
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        async with httpx.AsyncClient(base_url=self._base_url) as client:
            response = await client.post(
                f"/api/v3/envelopes?access_token={self._auth_token}",
                json={
                    "data": {
                        "type": envelope.type,
                        "attributes": {
                            "name": envelope.name,
                            "locale": envelope.locale,
                            "auto_close": envelope.auto_close,
                            "remind_interval": envelope.remind_interval,
                            "block_after_refusal": envelope.block_after_refusal,
                            "deadline_at": envelope.deadline_at,
                        },
                    }
                },
                headers=headers,
            )
            return response.json()

    async def activate_envelope(self, envelope: Envelope) -> dict:
        headers = {
            "Authorization": f"Bearer {self._auth_token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        async with httpx.AsyncClient(base_url=self._base_url) as client:
            response = await client.patch(
                f"/api/v3/envelopes/{envelope.id}?access_token={self._auth_token}",
                json={
                    "data": {
                        "type": envelope.type,
                        "attributes": {
                            "name": envelope.status,
                        },
                    }
                },
                headers=headers,
            )
            return response.json()
