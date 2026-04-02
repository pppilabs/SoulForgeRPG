"""Состояние героя и противников."""

from dataclasses import dataclass


@dataclass
class CharacterState:
    """Хранит базовые характеристики сущности."""

    name: str
    health: int
    stamina: int
    strength: int
    armor: int
