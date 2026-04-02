"""Модуль искусственного интеллекта противников.

Содержит простую стратегию выбора действия врага на основе расстояния
до персонажа игрока.
"""


class EnemyAI:
    """Выбирает действие врага на очередном игровом такте."""

    def choose_action(self, distance_to_player: int) -> str:
        """Возвращает тип поведения противника.

        Args:
            distance_to_player: Расстояние от противника до игрока.

        Returns:
            Строковый идентификатор действия: attack или advance.
        """

        if distance_to_player <= 2:
            return "attack"
        return "advance"
