import os
import tempfile
import whisper
from fastapi import UploadFile

from src.services.base import Service


class SpeechRecognitionConfig:
    model_name: str = "tiny"
    fp16: bool = False


default_config = SpeechRecognitionConfig()


class SpeechRecognitionService(Service):
    def __init__(self, config: SpeechRecognitionConfig = default_config):
        self.model = whisper.load_model(config.model_name)
        self.fp16 = config.fp16

    def transcribe(self, audio_file) -> str:
        # Create a temporary file to save the uploaded content
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_file:
            # If it's an UploadFile, read from file attribute
            if isinstance(audio_file, UploadFile):
                content = audio_file.file.read()
            else:
                # If it's already a file-like object
                content = audio_file.read()
            
            # Write the content to the temporary file
            temp_file.write(content)
            temp_file.flush()
            
            try:
                # Use the temporary file path for transcription
                result = self.model.transcribe(temp_file.name, fp16=self.fp16)
                return result["text"]
            finally:
                # Clean up the temporary file
                os.unlink(temp_file.name)


__all__ = ["SpeechRecognitionService", "SpeechRecognitionConfig"]
