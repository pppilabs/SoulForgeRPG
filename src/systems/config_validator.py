"""Проверка корректности настроек."""


def validate_resolution(width: int, height: int) -> bool:
    """Проверяет допустимость разрешения окна."""

    return width >= 800 and height >= 600
