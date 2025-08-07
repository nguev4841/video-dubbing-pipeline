import os

# Import both TTS engines
from scripts import tts_tortoise
from scripts import tts_elevenlabs

def synthesize_speech(text, speaker_name="default", output_path="output.wav", engine="tortoise"):
    if engine == "tortoise":
        print("[TTS] Using Tortoise TTS...")
        tts_tortoise.synthesize(text, speaker_name, output_path)
    elif engine == "elevenlabs":
        print("[TTS] Using ElevenLabs TTS...")
        tts_elevenlabs.synthesize(text, output_path)
    else:
        raise ValueError(f"Unknown TTS engine: {engine}")
