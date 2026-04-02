"""Точка входа проекта SoulForgeRPG."""

from src.ui.main_window import MainWindow
from src.systems.game_settings import get_default_settings


def main() -> None:
    """Запускает демонстрационную инициализацию проекта."""

    settings = get_default_settings()
    window = MainWindow(title="SoulForgeRPG", resolution=settings["resolution"])
    print(f"Запуск {window.title} в разрешении {window.resolution}")


if __name__ == "__main__":
    main()
