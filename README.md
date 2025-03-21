# Compress Audio and Convert to Base64

Just a simple script that compresses a audio file and prints out Base64 data, useful for me.

## Requirements

### System Requirements
- Python 3.x
- FFmpeg

### Python Dependencies
- pydub (>= 0.25.1)

## Installation

1. Install FFmpeg on your system:
   - Ubuntu/Debian: `sudo apt-get install ffmpeg`
   - macOS (with Homebrew): `brew install ffmpeg`
   - Windows: Download from [FFmpeg website](https://ffmpeg.org/download.html) or use Chocolatey: `choco install ffmpeg`

2. Install pydub `pip install pydub` or `sudo apt install python3-pydub`
## Usage

1. Download sound_to_base64.py
2. Run it with
```bash
python3 sound_to_base64.py
```
3. Input a path, enter, and a bitrate, enter, and it will output the base64 data

# Example
```bash
python3 sound_to_base64.py
Enter audio path: /home/johsmith/downloads/dogbark.mp3
Enter bitrate (default 64k): 40k

Compressed audio in Base64:
data:audio/mp3;base64,SUQzBAAAAAAAI1RTU0UAAAAPAAADTGF2ZjU5LjI3L/cutofftherest
```

## Supported Audio Formats

- MP3 (.mp3)
- WAV (.wav)
- OGG (.ogg)
- FLAC (.flac)
- M4A (.m4a)
- WMA (.wma)
- AAC (.aac) 

