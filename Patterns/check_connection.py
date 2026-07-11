from Patterns.errors import WinError

from urllib.request import urlopen

from urllib.error import URLError



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