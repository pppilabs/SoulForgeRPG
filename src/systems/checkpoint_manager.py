"""Контрольные точки игрового прогресса."""


class CheckpointManager:
    """Работает со списком открытых контрольных точек."""

    def __init__(self) -> None:
        self.unlocked_checkpoints: list[str] = []

    def unlock(self, checkpoint_name: str) -> None:
        """Добавляет новую контрольную точку."""

        self.unlocked_checkpoints.append(checkpoint_name)
