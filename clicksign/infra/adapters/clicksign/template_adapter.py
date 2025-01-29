from dataclasses import asdict, dataclass

from app.core.config import settings
from app.http.http_client import HttpClient


@dataclass
class Attributes:
    name: str
    content_base64: str


@dataclass
class Data:
    type: str
    attributes: Attributes


@dataclass
class Root:
    data: Data


class TemplateModelClicksignAdapter:
    def __init__(
        self,
        http_client: HttpClient = HttpClient(),
        auth_token: str = settings.CLICKSIGN_API_KEY,
    ):
        self._http_client = http_client
        self._auth_token = auth_token

    def get_template_model(self, id: str) -> str:
        response = self._http_client.get(
            f"/api/v3/templates/{id}?access_token={self._auth_token}",
        )
        return response

    def create_template_model(self, data: dict) -> str:
        headers = {
            "Authorization": f"Bearer {self._auth_token}",
            "Content-Type": "application/vnd.api+json",
            "Accept": "application/vnd.api+json",
        }

        response = self._http_client.post(
            f"/api/v3/templates?access_token={self._auth_token}",
            json_data={"data": asdict(data)},
            headers=headers,
        )
        print({"data": asdict(data)})
        return response
