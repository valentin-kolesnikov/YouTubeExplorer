from SecondFunctions.output import output_videos, save_docx

from ForthFunctions.collecting_info import collect_videos_of_playlist

from InputData.PlaylistExplorer import playlist_URL_extract

from Patterns.collectingStats import collect_stats

from Patterns.save_history import log, log_error, clear

from Patterns.asyncRYD import ryd

from asyncio import run




def videos_of_playlists(history, youtube):
    clear()
    
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
    parsed_videos = output_videos(results, statrequest)
    log(history, "OUTPUT_VIDEOS", status="SUCCESS")
    

    choice, full_path = save_docx(parsed_videos, keywords=playlist_URL)
    log(history, "SAVE_DOCS", status="SUCCESS" if choice == "y" else "DECLINED", file_path=str(full_path) if choice == "y" else None)

    input("\nPress Enter to return...")
    log(history, "EXIT")
    
    return