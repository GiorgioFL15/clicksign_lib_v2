from uuid import UUID

from uuid_extensions import uuid7

from clicksign.application.create_document import CreateDocument, Input
from tests.infra.adapters.document.fake_document_adapter import FakeDocumentAdapter


async def test_ensure_CreateDocument_is_capable_of_creating_a_document() -> None:
    document_adapter = FakeDocumentAdapter()
    sut = CreateDocument(
        document_adapter=document_adapter,
    )
    input = Input(
        type="documents",
        filename="teste document",
        content_base64="rwerwr32424wsfw342",
        envelope_id=uuid7(),
        metadata={},
    )
    output = await sut.execute(input)
    assert output.id
    assert not output.errors


async def test_ensure_CreateDocument_raises_error_when_document_type_is_invalid() -> (
    None
):
    document_adapter = FakeDocumentAdapter()
    sut = CreateDocument(
        document_adapter=document_adapter,
    )
    input = Input(
        type="",
        filename="teste document",
        content_base64="rwerwr32424wsfw342",
        envelope_id=uuid7(),
        metadata={},
    )
    output = await sut.execute(input)
    assert not output.id
    assert output.errors
    assert "Tipo de documento inválido" in output.errors
