from Starter.KeyExplorer import youtube_api_key, window_title
from Starter.QuotaExplorer import test_quota
from Starter.OAuth2 import youtube_OAuth2

from Patterns.save_history import clear

from menu_pages import menu_page1, menu_page2

from sys import exit









if __name__ == "__main__":
    window_title("YouTube Explorer")

    youtube, exc_OAuth2 = youtube_OAuth2()
    if exc_OAuth2:
        youtube = youtube_api_key()

    if not test_quota(youtube):
        input("\nPress Enter to exit...")
        exit(1)

    
    current_page = 1
    while True:
        
        try:
            clear()
            print("=============  v1.3.0  =============")

            if current_page == 1:
                current_page = menu_page1(youtube, exc_OAuth2, current_page)
                
            elif current_page == 2:
                current_page = menu_page2(exc_OAuth2, current_page)

        except KeyboardInterrupt:
            pass