"""Система игровых уведомлений."""


class NotificationCenter:
    """Хранит сообщения для игрока."""

    def __init__(self) -> None:
        self.messages: list[str] = []

    def push(self, message: str) -> None:
        """Добавляет новое сообщение в очередь уведомлений."""

        self.messages.append(message)
