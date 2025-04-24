import pytest

from src.services.bpmn_generation import BpmnGenerationService
from src.services.speech_recognition import SpeechRecognitionService


@pytest.mark.asyncio
async def test_generate_bpmn():
    bpmn_generation = BpmnGenerationService()
    bpmn = await bpmn_generation.generate_bpmn(
        "Отрисуй процесс обработки заказа. Когда заказ поступает, проверяется"
        " наличие товара на складе. Если товар есть, происходит упаковка и"
        "отправка, если нет — заказ отменяется."
    )
    assert bpmn is not None
    assert bpmn["nodes"] is not None
    assert bpmn["edges"] is not None


def test_transcribe_audio():
    speech_recognition = SpeechRecognitionService()
    transcription = speech_recognition.transcribe("src/audioo.mp3")
    print(transcription)