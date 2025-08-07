# Main orchestration script
from scripts.transcribe import transcribe_audio
from scripts.translate import translate_text
from scripts.tts import generate_speech
from scripts.lipsync import apply_lipsync
from scripts.utils import extract_audio, combine_audio_with_video

INPUT_VIDEO = "input/input.mp4"
LANGUAGE_TO = "es"

if __name__ == "__main__":
    audio_path = extract_audio(INPUT_VIDEO)
    transcription = transcribe_audio(audio_path)
    translated_text = translate_text(transcription, to_lang=LANGUAGE_TO)
    tts_audio_path = generate_speech(translated_text)
    synced_video_path = apply_lipsync(INPUT_VIDEO, tts_audio_path)
    final_output = combine_audio_with_video(synced_video_path, tts_audio_path)
    print(f"✅ Done! Output: {final_output}")
