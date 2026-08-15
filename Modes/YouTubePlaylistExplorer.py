from Patterns.HistoryLogs import HistorySessions
from Patterns.save_history import clear, log
from PlaylistExplorer_InputData.Collection_of_Playlists import collection_of_playlists
from PlaylistExplorer_InputData.Videos_of_Playlists import videos_of_playlists


def launcherPlaylists(youtube, exc_OAuth2):
    history = HistorySessions("Playlist")

    while True:
        clear()
        
        question = input(
            "1. Collecting playlists\n" \
            "2. Collecting videos from the playlist\n" \
            "0. Go back to the start menu\n\n" \
            "Choose the number: "
            ).strip()
        
        while True:
            if question == "0":
                log(history, "EXIT")
                return
            
            elif question == "1":
                clear()
                log(history, "COLLECT_PLAYLISTS")

                collection_of_playlists(history, youtube, exc_OAuth2)
                break

            elif question == "2":
                clear()
                log(history, "COLLECT_VIDEOS")

                videos_of_playlists(history, youtube)
                break

            else:
                question = input("\nEnter again: ").strip()