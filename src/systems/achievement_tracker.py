"""Отслеживание игровых достижений."""


class AchievementTracker:
    """Хранит список разблокированных достижений."""

    def __init__(self) -> None:
        self.achievements: list[str] = []

    def unlock(self, achievement_name: str) -> None:
        """Добавляет достижение в журнал игрока."""

        self.achievements.append(achievement_name)
