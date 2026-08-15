from urllib.error import URLError
from urllib.request import urlopen

from Patterns.errors import WinError

TEST_URL = (
    "http://clients3.google.com/generate_204",
    "https://www.cloudflare.com",
    "https://www.microsoft.com"
)


def internet_available():
    while True:
        is_connected = False

        for url in TEST_URL:
            try:
                urlopen(url, timeout=3)
                is_connected = True
                break

            except (OSError, URLError):
                continue

        if is_connected:
            return True

        exc = OSError(11001, "No Internet connection available")
            
        if WinError(exc):
            continue