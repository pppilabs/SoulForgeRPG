"""Игровые настройки проекта SoulForgeRPG.

Модуль содержит значения по умолчанию для параметров интерфейса
и базовых опций запуска приложения.
"""

DEFAULT_THEME = "ashen"
UI_SCALE = 100
SHOW_HINTS = True
ENABLE_MINIMAP = True
DEFAULT_RESOLUTION = (1920, 1080)


def get_default_settings() -> dict:
    """Возвращает базовый набор игровых настроек.

    Returns:
        Словарь с темой оформления, масштабом интерфейса,
        подсказками, миникартой и разрешением окна.
    """

    return {
        "theme": DEFAULT_THEME,
        "ui_scale": UI_SCALE,
        "show_hints": SHOW_HINTS,
        "enable_minimap": ENABLE_MINIMAP,
        "resolution": DEFAULT_RESOLUTION,
    }