from clicksign.application.create_envelope import CreateEnvelope, Input
from tests.infra.adapters.envelope.fake_envelope_adapter import FakeEnvelopeAdapter


async def test_ensure_CreateEnvelope_is_capable_of_creating_a_envelope_with_signers() -> (
    None
):
    envelope_adapter = FakeEnvelopeAdapter()
    sut = CreateEnvelope(
        envelope_adapter=envelope_adapter,
    )
    input = Input(
        type="envelopes",
        name="Envelope Teste",
        locale=None,
        auto_close=None,
        remind_interval=None,
        block_after_refusal=None,
        deadline_at=None,
    )
    output = await sut.execute(input)
    assert output.id
    assert not output.errors
