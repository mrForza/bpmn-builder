from fastapi import APIRouter, UploadFile, Depends
from typing import Annotated, Any

from src.presentation.api.providers.main import get_voice_service
from src.domain.usecases.voice_usecase import VoiceService


voice_router = APIRouter(prefix="/voice", tags=["voice"])


@voice_router.post("/")
async def upload_audio_file(
    audio_file: UploadFile,
    voice_service: Annotated[VoiceService, Depends(get_voice_service)],
) -> dict[str, Any]:
    await voice_service.upload_file(audio_file.file)

    return {
        "file_name": audio_file.filename,
        "file_type": audio_file.content_type,
        "message": await voice_service.upload_file("qwe"),
    }


@voice_router.post("/text")
async def get_text(
    audio_file: UploadFile,
    voice_service: Annotated[VoiceService, Depends(get_voice_service)],
) -> dict[str, Any]:
    generated_text = await voice_service.convert_to_text(audio_file)

    return {"text": generated_text}
