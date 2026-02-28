import requests
import json

def evaluate_answer(question, answer):
    """
    Evaluates an interview answer using Ollama Llama3 and returns assessment scores and feedback.
    Returns a dictionary with:
        - technical_score: int (0-40)
        - communication_score: int (0-30)
        - confidence_score: int (0-30)
        - feedback: str
    If LLM response can't be parsed as JSON, returns zeroed scores and empty feedback.
    """
    url = "http://localhost:11434/api/generate"
    prompt = (
        "Evaluate the following interview answer based on the given question. "
        "Return ONLY a strict JSON object in the following format (and no extra words):\n"
        "{\n"
        '  "technical_score": number (0-40),\n'
        '  "communication_score": number (0-30),\n'
        '  "confidence_score": number (0-30),\n'
        '  "feedback": "short overall feedback string"\n'
        "}\n"
        "Question:\n"
        f"{question}\n"
        "Answer:\n"
        f"{answer}\n"
    )
    payload = {
        "model": "mistral:latest",
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(url, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()
        content = result.get("response", "").strip()
        # attempt to locate JSON substring
        first_brace = content.find('{')
        last_brace = content.rfind('}')
        if first_brace != -1 and last_brace != -1 and last_brace > first_brace:
            json_str = content[first_brace:last_brace + 1]
            scores = json.loads(json_str)
            # Ensure keys are present and valid types
            technical = int(scores.get("technical_score", 0))
            communication = int(scores.get("communication_score", 0))
            confidence = int(scores.get("confidence_score", 0))
            feedback = scores.get("feedback", "")
            return {
                "technical_score": technical,
                "communication_score": communication,
                "confidence_score": confidence,
                "feedback": str(feedback)
            }
    except Exception:
        pass
    # fallback if any error
    return {
        "technical_score": 0,
        "communication_score": 0,
        "confidence_score": 0,
        "feedback": ""
    }