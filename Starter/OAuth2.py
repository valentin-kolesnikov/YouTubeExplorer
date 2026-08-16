import sys
from glob import glob
from pathlib import Path

from google.auth.exceptions import TransportError
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from Patterns.check_connection import internet_available
from Patterns.errors import WinError

link = ["https://www.googleapis.com/auth/youtube.readonly",
        "https://www.googleapis.com/auth/youtube.force-ssl"]


if getattr(sys, "frozen", False):
    app_folder = Path(sys.executable).parent
else:
    app_folder = Path(__file__).parent


key_folder = Path(app_folder, "Keys")
key_folder.mkdir(parents=True, exist_ok=True)


token_dir = Path(key_folder, "Client_token.json")


def credentials(client_file):
    credits = None

    if Path(token_dir).exists():
        credits = Credentials.from_authorized_user_file(token_dir, link)
    

    if not credits or not credits.valid:
        if credits and credits.expired and credits.refresh_token:
            credits.refresh(Request())

        else:    
            delivery = InstalledAppFlow.from_client_secrets_file(Path(key_folder, client_file), link)
            credits = delivery.run_local_server(port=8080)

            with open(token_dir, "w") as ct:
                ct.write(credits.to_json())
    
    return credits


def youtube_OAuth2():
    while True:
        try:
            file = glob(str(Path(key_folder, "client_secret_*.json")))

            if not file:
                raise FileNotFoundError

            client_file = file[0] 
            

            credits = credentials(client_file)


            OAuth2youtube = build("youtube", "v3", credentials=credits)

            return OAuth2youtube, False
        
        
        except FileNotFoundError:

            # the error message won't be displayed in the terminal, remember it

            return {}, True
        
        
        except TransportError, WinError:

            internet_available()


        except Exception as exc:

            print(f"\n\u001b[31mException: {exc}\u001b[0m")

            Path(token_dir).unlink(missing_ok=True)

            input('''\nReview the error message.
                  \nIf the issue is "Token has been expired", try to restart the application.
                  \n\nPress Enter to continue...''')
            print("\033[H\033[J", end="")

            return {}, True