# Spotify to YouTube MP3 Downloader

This project allows you to download songs or albums from Spotify by searching for them on YouTube and extracting their audio as MP3 files.

## Features
- Extract song and album information from Spotify.
- Search for the song on YouTube.
- Download the best available audio format and convert it to MP3.
- Simple GUI for easy usage.

## Installation
### Prerequisites
Make sure you have the following installed on your system:
- Python 3.7+
- `pip` (Python package manager)
- Google Chrome & ChromeDriver (for Selenium to work)
- FFmpeg (for audio conversion)

### Installing Dependencies
Run the following command to install the required packages:
```sh
pip install -r requirements.txt
```

### Setting Up FFmpeg
Ensure that FFmpeg is installed and accessible. You can download it from [FFmpeg's official website](https://ffmpeg.org/download.html).
If installed manually, specify its path in the script:
```python
'ffmpeg_location': "C:\\Program Files\\ffmpeg-master-latest-win64-gpl\\bin"
```

## Usage
### Running the Application
Execute the following command:
```sh
python python/app.py
```

### Using the GUI
1. Enter a **Spotify song or album URL**.
2. Click **"Download MP3 SONG"** to download a single song or **"Download MP3 ALBUM"** to download an album.

### Notes
- The script will automatically search for the song on YouTube and extract the best available audio.
- If no match is found, it will skip the download for that song.

## Troubleshooting
- If ChromeDriver fails, make sure it's updated to match your Chrome version.
- If Selenium throws an error about a sandbox issue on Windows, try running:
  ```sh
  chrome.exe --no-sandbox
  ```
- If FFmpeg errors occur, confirm that its path is correctly set.
- If you download a SONG when you wrote an ALBUM URL the program will crash, and vice versa.
- Sometimes at rare scenarios, it will download ads...

## Acknowledgments
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for downloading YouTube content.
- [Selenium](https://www.selenium.dev/) for web automation.
- [Pytube](https://pytube.io/en/latest/) for additional YouTube processing.

