from tests.infra.adapters.signer.fake_signer_adapter import FakeSignerAdapter 
from clicksign.application.create_signer import CreateSigner, Input


async def test_ensure_CreateSigner_is_capable_of_creating_a_signer() -> None:
    signer_adapter = FakeSignerAdapter()
    sut = CreateSigner(
        signer_adapter=signer_adapter,
    )
    input = Input(
        type="signers",
        name="Signatário de teste",
        birthday="1990-01-01",
        email="signer@example.com",
        phone_number="11999999999",
        has_documentation=True,
        documentation={"cpf": "12345678909"},
        refusable=False,
        group="Grupo de teste",
        envelope_id="fake-envelope-id"
        )
    output = await sut.execute(input)
    assert output.id
    assert not output.errors