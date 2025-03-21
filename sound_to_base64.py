#!/usr/bin/env python3

import base64
import os
from io import BytesIO

try:
    from pydub import AudioSegment
except ImportError:
    print("pydub not found. Install it: pip install pydub")
    exit(1)

def get_audio_format(file_path):
    extension = os.path.splitext(file_path)[1].lower()
    formats = {
        '.mp3': 'mp3',
        '.wav': 'wav', 
        '.ogg': 'ogg',
        '.flac': 'flac',
        '.m4a': 'm4a',
        '.wma': 'wma',
        '.aac': 'aac'
    }
    return formats.get(extension, 'mp3')

def compress_and_convert_to_base64(audio_path, bitrate="64k"):
    try:
        input_format = get_audio_format(audio_path)
        audio = AudioSegment.from_file(audio_path, format=input_format)
        buffer = BytesIO()
        
        # Convert to mp3 for web compatibility
        output_format = 'mp3'
        audio.export(buffer, format=output_format, bitrate=bitrate)
        return base64.b64encode(buffer.getvalue()).decode("utf-8"), output_format
    except FileNotFoundError:
        print(f"File not found: {audio_path}")
        exit(1)
    except Exception as e:
        print(f"Error processing audio: {e}")
        exit(1)

def main():
    audio_path = input("Enter audio path: ").strip()
    if not audio_path or not os.path.exists(audio_path):
        print("Invalid file path.")
        return

    bitrate = input("Enter bitrate (default 64k): ").strip() or "64k"
    b64_str, output_format = compress_and_convert_to_base64(audio_path, bitrate)
    print("\nCompressed audio in Base64:")
    print(f"data:audio/{output_format};base64,{b64_str}")

if __name__ == "__main__":
    main()
