import yt_dlp

def list_formats(url):
    ydl_opts = {
        'quiet': True,
        'nocheckcertificate': True,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
         # 'cookiefile': 'cookies.txt',  # Uncomment and set path if you want to use browser cookies
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        formats = info.get('formats', [])

        option_map = {}
        print("\nAvailable options:")

        # Collect video-only formats (video codec present, no audio codec)
        combo_formats = {}
        for f in formats:
            
            if f.get('vcodec') != 'none' and f.get('acodec') == 'none':
                res = f.get('height')
                if res:
                    combo_formats[res] = {'video': f['format_id'], 'audio': None}

        # Add best audio format to every video resolution
        for f in formats:
            if f.get('vcodec') == 'none' and f.get('acodec') != 'none':
                for res in combo_formats:
                    combo_formats[res]['audio'] = f['format_id']

        sorted_res = sorted(combo_formats.keys())
        idx = 1
        for res in sorted_res:
            video_id = combo_formats[res]['video']
            audio_id = combo_formats[res]['audio']
            option_map[idx] = {
                'desc': f"Video {res}p + Best Audio",
                'format_code': f"{video_id}+{audio_id}"
            }
            print(f"{idx}. {option_map[idx]['desc']}")
            idx += 1

       # Collect audio-only formats
        audio_formats = [f for f in formats if f.get('vcodec') == 'none' and f.get('acodec') != 'none']
        # Sort audio formats by average bitrate (abr)
        audio_formats = sorted(audio_formats, key=lambda x: x.get('abr') or 0, reverse=True)

        for f in audio_formats:
            abr = f.get('abr') or 0
            option_map[idx] = {
                'desc': f"Audio only - {abr:.3f} kbps",
                'format_code': f['format_id']
            }
            print(f"{idx}. {option_map[idx]['desc']}")
            idx += 1

        return option_map, info.get('title')

def download_selected(url, option_map, title):
    while True:
        try:
            choice = int(input("\nEnter the number of the option you want to download: "))
            if choice in option_map:
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Please enter a number.")

    format_code = option_map[choice]['format_code']

    ydl_opts = {
        'format': format_code,
        'outtmpl': f'{title}.%(ext)s',
        'merge_output_format': 'mp4',
        'nocheckcertificate': True,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
         # 'cookiefile': 'cookies.txt',  # Uncomment if using cookies
        'progress_hooks': [progress_hook],
    }

    print(f"\nDownloading {option_map[choice]['desc']}...")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("\n✅ Download completed!")

def progress_hook(d):
    if d['status'] == 'downloading':
        total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
        downloaded_bytes = d.get('downloaded_bytes', 0)
        if total_bytes:
            percent = downloaded_bytes / total_bytes * 100
            print(f"\rDownloading... {percent:.2f}%", end='', flush=True)
    elif d['status'] == 'finished':
        print("\nDownload finished, now processing...")

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ").strip()
    option_map, title = list_formats(video_url)
    download_selected(video_url, option_map, title)
