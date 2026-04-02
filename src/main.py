"""Точка входа проекта SoulForgeRPG.

Модуль подготавливает базовые настройки приложения и демонстрирует
инициализацию главного окна игровой программы.
"""

from src.ui.main_window import MainWindow
from src.systems.game_settings import get_default_settings


def main() -> None:
    """Запускает демонстрационную инициализацию проекта.

    Функция получает набор стандартных настроек, создаёт главное окно
    приложения и выводит в консоль информацию о параметрах запуска.
    """

    settings = get_default_settings()
    window = MainWindow(title="SoulForgeRPG", resolution=settings["resolution"])
    print(f"Запуск {window.title} в разрешении {window.resolution}")


if __name__ == "__main__":
    main()
