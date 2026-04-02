"""Сохранение и загрузка прогресса."""

from pathlib import Path


class SaveManager:
    """Работает с файлами игровых сохранений."""

    def __init__(self, save_dir: str = "saves") -> None:
        self.save_dir = Path(save_dir)

    def get_slot_path(self, slot_name: str) -> Path:
        """Возвращает путь к слоту сохранения."""

        return self.save_dir / f"{slot_name}.sav"
