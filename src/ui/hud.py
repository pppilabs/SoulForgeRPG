"""Экранные индикаторы персонажа."""


class HeadsUpDisplay:
    """Управляет отображением здоровья и выносливости."""

    def __init__(self) -> None:
        self.health = 100
        self.stamina = 100
        self.souls = 0

    def update(self, health: int, stamina: int, souls: int) -> None:
        """Обновляет значения интерфейсных индикаторов."""

        self.health = health
        self.stamina = stamina
        self.souls = souls
