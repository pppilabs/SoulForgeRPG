"""Журналирование игровых событий."""


class EventLogger:
    """Собирает сообщения о действиях системы."""

    def __init__(self) -> None:
        self.entries: list[str] = []

    def log(self, message: str) -> None:
        """Добавляет запись в журнал."""

        self.entries.append(message)
