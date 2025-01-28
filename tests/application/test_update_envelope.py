from tests.infra.adapters.envelope.fake_envelope_adapter import FakeEnvelopeAdapter
from clicksign.application.update_envelope import UpdateEnvelope, Input


async def test_ensure_UpdateEnvelope_is_capable_of_activating_an_envelope() -> None:
    envelope_adapter = FakeEnvelopeAdapter()
    sut = UpdateEnvelope(
        envelope_adapter=envelope_adapter,
    )
    input = Input(type="envelopes",
            status="running")
    output = await sut.execute(input)
    assert output.id
    assert not output.errors

async def test_ensure_UpdateEnvelope_raises_error_when_envelope_status_is_invalid() -> None:
    envelope_adapter = FakeEnvelopeAdapter()
    sut = UpdateEnvelope(
        envelope_adapter=envelope_adapter,
    )
    input = Input(type="envelopes",
            status="inativo")
    output = await sut.execute(input)
    assert not output.id
    assert output.errors
    assert "Envelope não pode ser ativado" in output.errors