import whisper


# загрузка модели.
# лучше использовать как минимум 'small'
model = whisper.load_model("tiny")
result = model.transcribe("audioo.mp3")
print(result["text"])

