from domain.interfaces.repositories.voice_repositories import (
    VoiceStorageRepository,
    VoiceDatabaseRepository,
)


class VoiceToTextTransformer:
    pass


class VoiceService:
    def __init__(
        self,
        db_repo: VoiceDatabaseRepository,
        storage_repo: VoiceStorageRepository,
        voice_transformer: VoiceToTextTransformer,
    ):
        self.db_repo = db_repo
        self.storage_repo = storage_repo
        self.voice_transformer = voice_transformer

    async def upload_file(self, audio_file) -> None:
        await self.storage_repo.save_file(audio_file)
        # await self.db_repo.save_file()

    async def convert_to_text(self, audio_file) -> str:  # type: ignore[empty-body]
        pass
