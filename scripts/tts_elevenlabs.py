import os
import requests
import json
from pathlib import Path

ELEVENLABS_API_KEY = "sk_3c438e1d15e15aa72485c0d29ce60edf2db31c4d7f75fe32"
ELEVENLABS_API_URL = "https://api.elevenlabs.io/v1/text-to-speech"

OUTPUT_DIR = Path("output/audio")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# You can optionally set a specific voice_id, or leave as None to let the script auto-pick.
DEFAULT_VOICE_ID = None  # Example: "21m00Tcm4TlvDq8ikWAM"  (Rachel)

def list_voices():
    response = requests.get(
        "https://api.elevenlabs.io/v1/voices",
        headers={"xi-api-key": ELEVENLABS_API_KEY}
    )
    response.raise_for_status()
    return response.json()["voices"]

def get_best_matching_voice(language="ko"):
    voices = list_voices()
    # Simple heuristic: choose first Korean voice or fallback
    for voice in voices:
        if language in (voice.get("labels") or {}).get("language", ""):
            return voice["voice_id"]
    return voices[0]["voice_id"] if voices else None

def generate_speech(text, filename, voice_id=None, language="ko"):
    if not voice_id:
        voice_id = get_best_matching_voice(language)
        print(f"Auto-selected voice: {voice_id}")

    url = f"{ELEVENLABS_API_URL}/{voice_id}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    response.raise_for_status()

    audio_path = OUTPUT_DIR / filename
    with open(audio_path, "wb") as f:
        f.write(response.content)
    print(f"Saved ElevenLabs audio to {audio_path}")
    return audio_path

# Example use:
if __name__ == "__main__":
    sample_text = "안녕하세요. 이것은 ElevenLabs를 사용한 테스트입니다."
    generate_speech(sample_text, "sample_ko.mp3")
