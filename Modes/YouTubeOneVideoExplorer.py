from Patterns.asyncRYD import ryd

from Patterns.EnteringURL import youtube_id_finder

from Patterns.collectingStats import collect_stats

from Patterns.check_connection import internet_available

from Patterns.HistoryLogs import HistorySessions

from Patterns.save_history import log, log_error, clear

from SecondFunctions.output import output_videos

from asyncio import run





def launcherInfo(youtube):
    history = HistorySessions("One Video Info")


    video_id = youtube_id_finder()
    log(history, "ENTER_VIDEO_LINK", video_link="https://www.youtube.com/watch?v=" + video_id)


    internet_available()
    log(history, "CHECK_INTERNET")

    
    statrequest, exc = collect_stats(youtube, [video_id])
    if exc:
        log_error(history, statrequest, exc)
        clear()

        return

    results = run(ryd([video_id]))

    log(history, "COLLECT_ONE_VIDEO_INFO", status="SUCCESS")
    clear()

    output_videos(results, statrequest, one_video_info=True)
    log(history, "OUTPUT_ONE_VIDEO_INFO", status="SUCCESS")

    input("\n\nPress Enter to return...")
    log(history, "EXIT")