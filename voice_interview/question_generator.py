import requests
import json
import re

def generate_questions(resume_text, num_questions=1):
    url = "http://localhost:11434/api/generate"

    prompt = f"""
Generate exactly {num_questions} interview questions.
Mix technical and behavioral.

Return ONLY JSON in this format:

{{
  "questions": ["q1","q2"]
}}

Resume:
{resume_text}
"""

    payload = {
        "model": "mistral:latest",   # FAST MODEL
        "prompt": prompt,
        "stream": False,
        "temperature": 0.2
    }

    try:
        response = requests.post(url, json=payload, timeout=180)
        result = response.json()
        content = result.get("response", "").strip()

        match = re.search(r'\{.*\}', content, re.DOTALL)
        if match:
            data = json.loads(match.group())
            return data.get("questions", [])

    except Exception as e:
        print("QUESTION ERROR:", e)

    return []