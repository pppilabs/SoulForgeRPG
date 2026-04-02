"""Модуль главного окна приложения SoulForgeRPG.

Содержит минимальную модель главного окна, которая используется
для демонстрации пользовательского интерфейса проекта.
"""


class MainWindow:
    """Представляет главное окно приложения.

    Attributes:
        title: Текст заголовка окна.
        resolution: Разрешение окна в пикселях.
        visible: Флаг отображения окна пользователю.
    """

    def __init__(self, title: str, resolution: tuple[int, int]) -> None:
        """Инициализирует главное окно приложения.

        Args:
            title: Заголовок игрового окна.
            resolution: Кортеж с шириной и высотой окна.
        """
        self.title = title
        self.resolution = resolution
        self.visible = False

    def show(self) -> None:
        """Отображает окно приложения пользователю."""

        self.visible = True
