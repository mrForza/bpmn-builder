from fastapi import APIRouter, UploadFile, File, Depends
from typing import Annotated
from src.domain.usecases.voice_usecase import VoiceService

main_router = APIRouter()


@main_router.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}


@main_router.post("/voice-to-text")
async def voice_to_text(file: UploadFile):
    return {"status": "ok"}


@main_router.post("/text-to-bpmn")
async def text_to_bpmn(text: str):
    return {"status": "ok"}
