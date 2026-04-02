"""Регистрация и загрузка игровых ресурсов."""


class ResourceRegistry:
    """Хранит имена доступных ресурсов проекта."""

    def __init__(self) -> None:
        self.resources: dict[str, str] = {}

    def register(self, key: str, path: str) -> None:
        """Сохраняет путь к ресурсу."""

        self.resources[key] = path
