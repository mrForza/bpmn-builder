import whisper

from src.services.base import Service


class SpeechRecognitionConfig:
    model_name: str = "tiny"
    fp16: bool = False


default_config = SpeechRecognitionConfig()


class SpeechRecognitionService(Service):
    def __init__(self, config: SpeechRecognitionConfig = default_config):
        self.model = whisper.load_model(config.model_name)
        self.fp16 = config.fp16

    def transcribe(self, audio_file: str) -> str:
        result = self.model.transcribe(audio_file, fp16=self.fp16)
        return result["text"]


__all__ = ["SpeechRecognitionService", "SpeechRecognitionConfig"]
