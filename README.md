# YouTube Downloader with Format Selection

A Python script that uses **yt\_dlp** to list and download YouTube videos with options for separate video + audio or audio-only formats. Supports merging formats with **ffmpeg**, shows download progress, and handles user-agent & certificates.


## Features

* Lists available video resolutions with best audio.
* Lists audio-only formats by bitrate.
* Download your selected format with auto merging.
* Supports cookies (optional).
* Shows download progress.
* Handles common errors gracefully.

## Requirements

* Python 3.7 or higher
* [yt\_dlp](https://github.com/yt-dlp/yt-dlp) Python package
* [ffmpeg](https://ffmpeg.org/download.html) installed and added to system PATH

## Installation

### 1. Install Python

Download and install Python from [python.org](https://www.python.org/downloads/). Ensure you add Python to your system PATH during installation.

### 2. Install yt\_dlp

Open a terminal (Command Prompt or PowerShell) and run:

```bash
pip install yt-dlp
```

### 3. Install ffmpeg

* Download ffmpeg for your OS from [ffmpeg.org](https://ffmpeg.org/download.html#build-windows).
* Extract the folder.
* Add the `bin` folder containing `ffmpeg.exe` to your system PATH environment variable.

To check, run:

```bash
ffmpeg -version
```

You should see ffmpeg version info.


## Usage

1. Save the Python script (e.g., `ytd.py`) on your computer.

2. Open terminal/command prompt in the script folder.

3. Run the script:

```bash
python ytd.py
```

4. Enter the YouTube video URL when prompted.

5. Choose from the listed video + audio or audio-only formats by entering the number.

6. The selected format will download, merging video and audio if needed.


## Optional Features

* **Use browser cookies:**
  If you want to download age-restricted or private videos, export your browser cookies to a file named `cookies.txt` and uncomment the `cookiefile` line in the script.

* **Customize user-agent:**
  The script already sets a modern browser user-agent string for better compatibility.


## Troubleshooting

* **`ffmpeg` not found error:**
  Make sure ffmpeg is installed and added to your system PATH.

* **HTTP 403 Forbidden errors:**
  Try updating yt\_dlp or use cookies if content is age-restricted.

* **Permission errors:**
  Run the terminal as administrator or check folder write permissions.

## License

This project is open-source under the MIT License.
