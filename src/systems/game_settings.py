"""Игровые настройки проекта."""

DEFAULT_THEME = "ember"
UI_SCALE = 115
SHOW_HINTS = True
ENABLE_MINIMAP = True
DEFAULT_RESOLUTION = (1920, 1080)


def get_default_settings() -> dict:
    """Возвращает базовый набор настроек."""

    return {
        "theme": DEFAULT_THEME,
        "ui_scale": UI_SCALE,
        "show_hints": SHOW_HINTS,
        "enable_minimap": ENABLE_MINIMAP,
        "resolution": DEFAULT_RESOLUTION,
    }