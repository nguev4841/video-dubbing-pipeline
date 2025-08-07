import requests
import time

ELEVENLABS_API_KEY = "sk_c7f6bcaecb5748089b52ed839a74a6e8eda2ffbc27be06ed"
ELEVENLABS_VOICE_ID = "21m00Tcm4TlvDq8ikWAM"  # Default voice, you can change if needed
ELEVENLABS_API_URL = "https://api.elevenlabs.io/v1/text-to-speech"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "xi-api-key": ELEVENLABS_API_KEY,
}

def tts_elevenlabs(text, voice_id=ELEVENLABS_VOICE_ID, output_path="output.wav"):
    payload = {
        "text": text,
        "voice_settings": {
            "stability": 0.75,
            "similarity_boost": 0.75
        }
    }

    url = f"{ELEVENLABS_API_URL}/{voice_id}/stream"

    response = requests.post(url, json=payload, headers=headers, stream=True)

    if response.status_code != 200:
        raise Exception(f"ElevenLabs TTS failed: {response.status_code} {response.text}")

    with open(output_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    # Optional small delay for API limits
    time.sleep(0.5)

    return output_path
