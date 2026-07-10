from Patterns.errors import WinError

from urllib.request import urlopen

from urllib.error import URLError



TEST_URL = (
    "http://clients3.google.com/generate_204",
    "https://www.cloudflare.com"
    "https://www.microsoft.com"
)


def internet_available():
    while True:
        try:
            urlopen(TEST_URL)
            return False

        except OSError as exc:
            
            if WinError(exc):
                continue

        except URLError as exc:
            print("The check server is likely unavailable.")
            if isinstance(exc.reason, OSError):
                WinError(exc.reason)