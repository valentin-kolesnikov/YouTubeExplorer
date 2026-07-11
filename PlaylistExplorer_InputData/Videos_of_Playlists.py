from SecondFunctions.output import output_videos

from ForthFunctions.collecting_info import collect_videos_of_playlist

from InputData.PlaylistExplorer import playlist_URL_extract

from Patterns.collectingStats import collect_stats

from Patterns.save_history import log, log_error, clear

from Patterns.asyncRYD import ryd

from asyncio import run




def videos_of_playlists(history, youtube):
    playlist_URL = playlist_URL_extract()
    log(history, "ENTER_PLAYLIST_LINK", playlist_link="https://www.youtube.com/playlist?list=" + playlist_URL)

    video_ids, exc = collect_videos_of_playlist(youtube, playlist_URL)
    if exc:
        log_error(history, video_ids, exc)
        clear()
        return
    
    results = run(ryd(video_ids))

    statrequest, exc = collect_stats(youtube, video_ids)
    if exc:
        log_error(history, statrequest, exc)
        clear()
        return
    
    log(history, "COLLECT_VIDEOS", status="SUCCESS")
    clear()

    print(f"https://www.youtube.com/playlist?list={playlist_URL}\n")
    output_videos(results, statrequest, keywords=None, one_video_info=False)
    log(history, "OUTPUT_VIDEOS")

    input("\nPress Enter to return...")
    log(history, "EXIT")
    
    return