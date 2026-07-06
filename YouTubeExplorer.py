from Modes.YouTubeCommentExplorer import launcherComments
from Modes.YouTubeVideoExplorer import launcherVideos
from Modes.YouTubeChannelExplorer import launcherChannels
from Modes.YouTubePlaylistExplorer import launcherPlaylists
from Modes.YouTubeSubtitlesExplorer import launcherSubtitles
from Modes.YouTubeOneVideoExplorer import launcherInfo
from Modes.YouTubeExplorerLicense import launcherABOUT, launcherLICENSE
from Modes.YouTubeASCIIExplorer import launcherASCII
from Modes.YouTubeHistoryExplorer import launcherHistory
from Modes.KeysAPI import launcherKey

from Starter.KeyExplorer import youtube_api_key, window_title
from Starter.QuotaExplorer import test_quota
from Starter.OAuth2 import youtube_OAuth2

from sys import exit









if __name__ == "__main__":
    window_title("YouTube Explorer")

    youtube, exc_OAuth2 = youtube_OAuth2()
    if exc_OAuth2:
        youtube = youtube_api_key()

    if not test_quota(youtube):
        input("\nPress Enter to exit...")
        exit(1)

    while True:
        try:
            current_page = 1
            while True:
                print("\033[H\033[J", end="")
                print("============  v1.2.0  ============")

                match current_page:
                    case 1:
                        print(f"Page {current_page}\n")

                        questionist1 = input(
                            "1. Comments\n" \
                            "2. Videos\n" \
                            "3. Channels\n" \
                            "4. Playlists\n" \
                            "5. Subtitles\n" \
                            "6. One Video Info\n\n" \
                            "0. Exit\n\n" \
                            "Enter the number (press Enter for next page): "
                        )
                        while True:
                            if questionist1 == "1":
                                print("\033[H\033[J", end="")
                                launcherComments(youtube)
                                break
                            elif questionist1 == "2":
                                print("\033[H\033[J", end="")
                                launcherVideos(youtube)
                                break
                            elif questionist1 == "3":
                                print("\033[H\033[J", end="")
                                launcherChannels(youtube)
                                break
                            elif questionist1 == "4":
                                print("\033[H\033[J", end="")
                                launcherPlaylists(youtube, exc_OAuth2)
                                break
                            elif questionist1 == "5":
                                print("\033[H\033[J", end="")
                                launcherSubtitles()
                                break
                            elif questionist1 == "6":
                                print("\033[H\033[J", end="")
                                launcherInfo(youtube)
                                break

                            elif questionist1 == "":
                                current_page = 2
                                break
                            elif questionist1 == "0":
                                exit(0)
                            else:
                                break
                            
                    case 2:
                        print(f"Page {current_page}\n")

                        questionist2 = input(
                            "1. YouTube API Key\n" \
                            "2. History\n" \
                            "3. ASCII Art\n" \
                            "4. LICENSE\n" \
                            "5. ABOUT\n\n" \
                            "0. Exit\n\n" \
                            "Enter the number (press Enter for prev page): "
                        )
                        
                        while True:
                            if questionist2 == "1":
                                print("\033[H\033[J", end="")
                                launcherKey(exc_OAuth2)
                                break
                            elif questionist2 == "2":
                                print("\033[H\033[J", end="")
                                launcherHistory()
                                break
                            elif questionist2 == "3":
                                print("\033[H\033[J", end="")
                                launcherASCII()
                                break
                            elif questionist2 == "4":
                                print("\033[H\033[J", end="")
                                launcherLICENSE()
                                break
                            elif questionist2 == "5":
                                print("\033[H\033[J", end="")
                                launcherABOUT()
                                break
                                
                            elif questionist2 == "":
                                current_page = 1
                                break
                            elif questionist2 == "0":
                                exit(0)
                            else:
                                break
                            

        except KeyboardInterrupt:
            pass