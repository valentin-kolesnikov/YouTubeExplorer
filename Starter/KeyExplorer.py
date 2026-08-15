import sys
from pathlib import Path

from googleapiclient.discovery import build


def window_title(title):
    if sys.stdout.isatty():
        sys.stdout.write(f"\33]0;{title}\a")
        sys.stdout.flush()




if getattr(sys, "frozen", False):
    app_folder = Path(sys.executable).parent
else:
    app_folder = Path(__file__).parent


key_folder = Path(app_folder, "Keys")
key_folder.mkdir(parents=True, exist_ok=True)


key_file = Path(key_folder, "Key.bin")


class memory():

    def save_key(api_key):
        with open(key_file, "wb") as f:
            f.write(api_key.encode("utf-8"))


    def load_key():
        if key_file.exists():
            with open(key_file, "rb") as f:
                return f.read().decode("utf-8")
        return None



def youtube_api_key():
    api_key = memory.load_key()

    if not api_key:
        api_key = input("Enter your YouTube API key: ").strip()

        while len(api_key) != 39:
            api_key = input("\nThis is not the YouTube API key. Try entering the API key again: ").strip()
        memory.save_key(api_key)

    youtube = build('youtube', 'v3', developerKey=api_key, static_discovery=False)
    
    return youtube
