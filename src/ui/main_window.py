"""Главное окно приложения."""


class MainWindow:
    """Описывает базовые параметры главного окна игры."""

    def __init__(self, title: str, resolution: tuple[int, int]) -> None:
        self.title = title
        self.resolution = resolution
        self.visible = False

    def show(self) -> None:
        """Показывает окно пользователю."""

        self.visible = True
