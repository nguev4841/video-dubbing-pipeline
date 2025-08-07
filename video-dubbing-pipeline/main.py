import os
from scripts import transcribe, translate, tts, lipsync

INPUT_VIDEO = "myvideo.mp4"
OUTPUT_VIDEO = "dubbed_video.mp4"
LANG_SOURCE = "ko"  # Korean
LANG_TARGET = "en"  # English
TTS_ENGINE = "elevenlabs"  # Change to "tortoise" to use Tortoise TTS

TEMP_DIR = "temp"
os.makedirs(TEMP_DIR, exist_ok=True)

# Step 1: Transcribe
transcript_path = os.path.join(TEMP_DIR, "transcript.txt")
transcribe.transcribe_audio(INPUT_VIDEO, transcript_path, language=LANG_SOURCE)

# Step 2: Translate
translated_path = os.path.join(TEMP_DIR, "translated.txt")
translate.translate_text(transcript_path, translated_path, src_lang=LANG_SOURCE, tgt_lang=LANG_TARGET)

# Step 3: TTS
tts_audio_path = os.path.join(TEMP_DIR, "tts.wav")
with open(translated_path, "r", encoding="utf-8") as f:
    text = f.read()

tts.synthesize_speech(text, output_path=tts_audio_path, engine=TTS_ENGINE)

# Step 4: Lip-sync
lipsync.lipsync_video(INPUT_VIDEO, tts_audio_path, OUTPUT_VIDEO)

print(f"\n✅ Dubbing complete! Output saved as: {OUTPUT_VIDEO}")
