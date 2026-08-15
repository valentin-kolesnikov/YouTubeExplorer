from sys import exit

from Modes.KeysAPI import launcherKey
from Modes.YouTubeASCIIExplorer import launcherASCII
from Modes.YouTubeChannelExplorer import launcherChannels
from Modes.YouTubeCommentExplorer import launcherComments
from Modes.YouTubeExplorerLicense import launcherABOUT, launcherLICENSE
from Modes.YouTubeHistoryExplorer import launcherHistory
from Modes.YouTubeOneVideoExplorer import launcherInfo
from Modes.YouTubePlaylistExplorer import launcherPlaylists
from Modes.YouTubeSubtitlesExplorer import launcherSubtitles
from Modes.YouTubeVideoExplorer import launcherVideos
from Patterns.save_history import clear


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
    ).strip()

    page1 = {
        "1": lambda: launcherComments(youtube),
        "2": lambda: launcherVideos(youtube),
        "3": lambda: launcherChannels(youtube),
        "4": lambda: launcherPlaylists(youtube, exc_OAuth2),
        "5": lambda: launcherSubtitles(),
        "6": lambda: launcherInfo(youtube)
    }

    if questionist1 == "":
        current_page = 2

    elif questionist1 == "0":
        exit(0)

    elif questionist1 in page1:
        clear()
        page1[questionist1]()

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
    ).strip()

    page2 = {
        "1": lambda: launcherKey(exc_OAuth2),
        "2": lambda: launcherHistory(),
        "3": lambda: launcherASCII(),
        "4": lambda: launcherLICENSE(),
        "5": lambda: launcherABOUT()
    }

    if questionist2 == "":
        current_page = 1
        
    elif questionist2 == "0":
        exit(0)

    elif questionist2 in page2:
        clear()
        page2[questionist2]()

    return current_page