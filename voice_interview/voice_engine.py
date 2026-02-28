import whisper

print("Loading Whisper model...")

try:
    _whisper_model = whisper.load_model("tiny", device="cpu")
    print("Model loaded successfully.")
except Exception as e:
    print("MODEL LOAD ERROR:", e)
    _whisper_model = None


def transcribe_audio(file_path):
    print("Transcribing:", file_path)

    if _whisper_model is None:
        print("Model is None!")
        return ""

    try:
        result = _whisper_model.transcribe(file_path)
        #print("Raw result:", result)
        return result.get("text", "").strip()
    except Exception as e:
        print("TRANSCRIPTION ERROR:", e)
        return ""