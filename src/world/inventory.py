"""Инвентарь персонажа."""


class Inventory:
    """Управляет списком предметов героя."""

    def __init__(self) -> None:
        self.items: list[str] = []

    def add_item(self, item_name: str) -> None:
        """Добавляет предмет в инвентарь."""

        self.items.append(item_name)
