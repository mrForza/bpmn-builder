from src.domain.interfaces.repositories.voice_repositories import (
    VoiceStorageRepository,
)


class MinioVoiceRepository(VoiceStorageRepository):
    async def save_file(self, audio_file): ...

    async def get_all_files(self): ...

    async def get_file(self): ...
