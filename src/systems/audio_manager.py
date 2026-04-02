"""Управление звуком и музыкальным оформлением."""


class AudioManager:
    """Хранит параметры звука приложения."""

    def __init__(self) -> None:
        self.master_volume = 70
        self.music_enabled = True
