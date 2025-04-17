import whisper


model = whisper.load_model("tiny")
result = model.transcribe("audioo.mp3", fp16=False)
print(result["text"])

