"""Игровые настройки проекта."""

DEFAULT_THEME = "obsidian"
UI_SCALE = 90
SHOW_HINTS = False
ENABLE_MINIMAP = False
DEFAULT_RESOLUTION = (1600, 900)


def get_default_settings() -> dict:
    """Возвращает базовый набор настроек."""

    return {
        "theme": DEFAULT_THEME,
        "ui_scale": UI_SCALE,
        "show_hints": SHOW_HINTS,
        "enable_minimap": ENABLE_MINIMAP,
        "resolution": DEFAULT_RESOLUTION,
    }