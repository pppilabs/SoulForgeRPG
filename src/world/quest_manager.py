"""Подсистема квестов и сюжетных задач."""


class QuestManager:
    """Хранит активные задания игрока."""

    def __init__(self) -> None:
        self.active_quests: list[str] = []

    def add_quest(self, quest_name: str) -> None:
        """Добавляет квест в журнал."""

        self.active_quests.append(quest_name)
