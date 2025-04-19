from dataclasses import dataclass
from domain.interfaces.repositories.voice_repositories import (
    VoiceStorageRepository,
    VoiceDatabaseRepository,
)
from minio import Minio


@dataclass(frozen=True)
class MinioConfig:
    login: str
    password: str


@dataclass(frozen=True)
class PostgresConfig:
    login: str
    password: str
    database: str
    host: str
    port: int


class MinioVoiceRepository(VoiceStorageRepository):
    def __init__(self, config: MinioConfig):
        self.client = Minio(
            endpoint="localhost:9000",
            access_key=config.login,
            secret_key=config.password,
            secure=False,
        )

    async def save_file(self, audio_file):
        print(audio_file)

        if not self.client.bucket_exists("audio_files"):
            self.client.make_bucket("audio_files")

        # self.client.fput_object('audio_files', 'audio.mp3', )


class PostgresVoiceRepository(VoiceDatabaseRepository):
    async def save_metadata(self, metadata): ...

    async def get_metadata(self): ...
