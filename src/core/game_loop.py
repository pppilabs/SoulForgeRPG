"""Главный игровой цикл."""


class GameLoop:
    """Управляет состоянием выполнения игры."""

    def __init__(self, target_fps: int = 60) -> None:
        self.target_fps = target_fps
        self.running = False

    def start(self) -> None:
        """Запускает игровой цикл."""

        self.running = True
