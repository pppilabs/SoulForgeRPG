"""Игровые настройки проекта."""

DEFAULT_THEME = "ashen"
UI_SCALE = 100
SHOW_HINTS = True
DEFAULT_RESOLUTION = (1920, 1080)


def get_default_settings() -> dict:
    """Возвращает базовый набор настроек."""

    return {
        "theme": DEFAULT_THEME,
        "ui_scale": UI_SCALE,
        "show_hints": SHOW_HINTS,
        "resolution": DEFAULT_RESOLUTION,
    }
