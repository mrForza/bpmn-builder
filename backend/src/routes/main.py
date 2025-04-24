from fastapi import APIRouter, UploadFile
from typing import Annotated
from pydantic import BaseModel
from src.services.speech_recognition import SpeechRecognitionService
from src.services.bpmn_generation import BpmnGenerationService

main_router = APIRouter()


class TextToBpmnRequest(BaseModel):
    text: str


@main_router.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}


@main_router.post("/voice-to-text")
async def voice_to_text(file: UploadFile):
    speech_recognition = SpeechRecognitionService()
    transcription = speech_recognition.transcribe(file.file)
    return {"transcription": transcription}


@main_router.post("/text-to-bpmn")
async def text_to_bpmn(request: TextToBpmnRequest):
    bpmn_generation = BpmnGenerationService()
    bpmn = await bpmn_generation.generate_bpmn(request.text)
    return {"bpmn": bpmn}
