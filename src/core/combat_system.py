"""Модуль базовой боевой системы.

Содержит минимальную реализацию расчёта урона между атакующим
и защищающимся персонажами проекта SoulForgeRPG.
"""

from src.core.character_state import CharacterState


class CombatSystem:
    """Выполняет расчёт урона в боевых столкновениях."""

    def calculate_damage(self, attacker: CharacterState, defender: CharacterState) -> int:
        """Вычисляет итоговый урон после учёта защиты.

        Args:
            attacker: Персонаж, выполняющий атаку.
            defender: Персонаж, принимающий удар.

        Returns:
            Минимум 1 единица урона с учётом силы и брони.
        """

        return max(1, attacker.strength - defender.armor)
