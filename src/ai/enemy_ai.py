"""Простейшая логика поведения противника."""


class EnemyAI:
    """Выбирает действие врага на игровом такте."""

    def choose_action(self, distance_to_player: int) -> str:
        """Возвращает тип поведения противника."""

        if distance_to_player <= 2:
            return "attack"
        return "advance"
