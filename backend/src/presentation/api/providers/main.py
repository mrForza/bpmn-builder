from fastapi import FastAPI, Depends
from typing import Annotated

from src.infrastructure.database.repositories.voice import PostgresVoiceRepository
from src.infrastructure.object_storage.repositories.voice import (
    MinioVoiceRepository,
)
from src.domain.usecases.voice_usecase import VoiceService, VoiceToTextTransformer
from src.domain.interfaces.repositories.voice_repositories import (
    VoiceStorageRepository,
    VoiceDatabaseRepository,
)


def get_postgres_voice_repo() -> PostgresVoiceRepository:
    return PostgresVoiceRepository()


def get_minio_voice_repo() -> MinioVoiceRepository:
    return MinioVoiceRepository()


def get_voice_to_text_transformer() -> VoiceToTextTransformer:
    return VoiceToTextTransformer()


def get_voice_service(
    db_repo: Annotated[
        VoiceDatabaseRepository, Depends(get_postgres_voice_repo)
    ],
    storage_repo: Annotated[
        VoiceStorageRepository, Depends(get_minio_voice_repo)
    ],
    transformer: Annotated[
        VoiceToTextTransformer, Depends(VoiceToTextTransformer)
    ],
) -> VoiceService:
    return VoiceService(
        db_repo=db_repo,
        storage_repo=storage_repo,
        voice_transformer=transformer,
    )


def setup_providers(app: FastAPI):
    pass
