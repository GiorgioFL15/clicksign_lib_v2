from tests.infra.adapters.required_auth.fake_required_auth_adapter import FakeRequiredAuthAdapter 
from clicksign.application.create_required_auth import CreateRequiredAuth, Input


async def test_ensure_CreateBulkAuth_is_capable_of_creating_a_bulk_auth() -> None:
    required_auth_adapter = FakeRequiredAuthAdapter()
    sut = CreateRequiredAuth(
        required_auth_adapter=required_auth_adapter,
    )
    input = Input(
        type="bulk_requirements",
        first_opp="add",
        first_action="authenticate",
        auth="sms",
        second_opp="add",
        second_action="sign",
        role="signer",
        document_id="fake-document-id",
        signer_id="fake-signer-id",
        envelope_id="fake-envelope-id",
        )
    output = await sut.execute(input)
    assert output.id