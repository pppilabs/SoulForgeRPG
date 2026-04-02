"""Подсистема боевых столкновений."""

from src.core.character_state import CharacterState


class CombatSystem:
    """Выполняет расчёт получаемого урона."""

    def calculate_damage(self, attacker: CharacterState, defender: CharacterState) -> int:
        """Возвращает итоговый урон после учёта защиты."""

        return max(1, attacker.strength - defender.armor)
