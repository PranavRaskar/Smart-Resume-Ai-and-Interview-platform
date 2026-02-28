from .voice_engine import transcribe_audio
from .evaluator import evaluate_answer

def process_audio_answer(question, audio_path):
    """
    Complete interview pipeline:
    Audio → Transcription → Evaluation
    Returns:
    {
        "transcript": str,
        "technical_score": int,
        "communication_score": int,
        "confidence_score": int,
        "feedback": str
    }
    """

    # Step 1: Convert speech to text
    transcript = transcribe_audio(audio_path)

    # Step 2: Evaluate answer using Ollama
    evaluation = evaluate_answer(question, transcript)

    return {
        "transcript": transcript,
        **evaluation
    }