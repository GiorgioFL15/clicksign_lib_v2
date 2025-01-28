from uuid import UUID
from typing import Optional


class Envelope:
    def __init__(
        self,
        type: str,
        name: Optional[str] = None,
        locale: Optional[str] = None,
        auto_close: Optional[str] = None,
        remind_interval: Optional[str] = None,
        block_after_refusal: Optional[str] = None,
        deadline_at: Optional[str] = None,
        status: Optional[str] = None,
    ):  # RECUPERAR DO BANCO
        self._type = type
        self._name = name
        self._locale = locale
        self._auto_close = auto_close
        self._remind_interval = remind_interval
        self._block_after_refusal = block_after_refusal
        self._deadline_at = deadline_at
        self._status = status
        self._id = id
        self._signers: dict[str, UUID] = {}

    @staticmethod
    def create(
        type: str,
        name: Optional[str] = None,
        locale: Optional[str] = None,
        auto_close: Optional[str] = None,
        remind_interval: Optional[str] = None,
        block_after_refusal: Optional[str] = None,
        deadline_at: Optional[str] = None,
    ) -> "Envelope":
        envelope = Envelope(
            type=type,
            name=name,
            locale=locale,
            auto_close=auto_close,
            remind_interval=remind_interval,
            block_after_refusal=block_after_refusal,
            deadline_at=deadline_at,
        )
        return envelope

    @staticmethod
    def update(
        type: str,
        status: Optional[str] = None,
    ) -> "Envelope":
        envelope = Envelope(
            type=type,
            status=status,
        )
        return envelope

    @property
    def type(self) -> str:
        return self._type

    @property
    def name(self) -> Optional[str]:
        return self._name

    @property
    def locale(self) -> Optional[str]:
        return self._locale

    @property
    def auto_close(self) -> Optional[str]:
        return self._auto_close

    @property
    def remind_interval(self) -> Optional[str]:
        return self._remind_interval

    @property
    def block_after_refusal(self) -> Optional[str]:
        return self._block_after_refusal

    @property
    def deadline_at(self) -> Optional[str]:
        return self._deadline_at

    @property
    def signers(self) -> dict[str, UUID]:
        return self._signers
    
    @property
    def status(self) -> Optional[str]:
        return self._status

    @property
    def id(self) -> UUID:
        return self._id
