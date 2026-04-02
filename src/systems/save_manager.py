"""Сохранение и загрузка игрового прогресса.

Модуль инкапсулирует базовую работу с директориями и именами файлов,
используемых для хранения слотов сохранения.
"""

from pathlib import Path


class SaveManager:
    """Работает с файлами игровых сохранений.

    Attributes:
        save_dir: Каталог, в котором располагаются файлы сохранений.
    """

    def __init__(self, save_dir: str = "saves") -> None:
        """Создаёт менеджер сохранений.

        Args:
            save_dir: Путь к каталогу со слотами сохранения.
        """
        self.save_dir = Path(save_dir)

    def get_slot_path(self, slot_name: str) -> Path:
        """Возвращает путь к конкретному слоту сохранения.

        Args:
            slot_name: Имя слота без расширения файла.

        Returns:
            Полный путь к файлу сохранения.
        """

        return self.save_dir / f"{slot_name}.sav"
