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

from Patterns.save_history import clear

from sys import exit


def menu_page1(youtube, exc_OAuth2, current_page):
    
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
            clear()
            launcherComments(youtube)
            break
        elif questionist1 == "2":
            clear()
            launcherVideos(youtube)
            break
        elif questionist1 == "3":
            clear()
            launcherChannels(youtube)
            break
        elif questionist1 == "4":
            clear()
            launcherPlaylists(youtube, exc_OAuth2)
            break
        elif questionist1 == "5":
            clear()
            launcherSubtitles()
            break
        elif questionist1 == "6":
            clear()
            launcherInfo(youtube)
            break

        elif questionist1 == "":
            current_page = 2
            break
        elif questionist1 == "0":
            exit(0)
        else:
            break

    return current_page


                    
def menu_page2(exc_OAuth2, current_page):

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
            clear()
            launcherKey(exc_OAuth2)
            break
        elif questionist2 == "2":
            clear()
            launcherHistory()
            break
        elif questionist2 == "3":
            clear()
            launcherASCII()
            break
        elif questionist2 == "4":
            clear()
            launcherLICENSE()
            break
        elif questionist2 == "5":
            clear()
            launcherABOUT()
            break
            
        elif questionist2 == "":
            current_page = 1
            break
        elif questionist2 == "0":
            exit(0)
        else:
            break

    return current_page