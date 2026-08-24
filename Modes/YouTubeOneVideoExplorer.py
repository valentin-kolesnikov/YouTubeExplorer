from asyncio import run

from Patterns.asyncRYD import ryd
from Patterns.check_connection import internet_available
from Patterns.collectingStats import collect_stats
from Patterns.EnteringURL import youtube_id_finder
from Patterns.HistoryLogs import HistorySessions
from Patterns.save_history import clear, log, log_error
from SecondFunctions.output import output_videos, save_docx


def launcherInfo(youtube):
    history = HistorySessions("One Video Info")


    video_id = youtube_id_finder()
    log(history, "ENTER_VIDEO_LINK", video_link="https://www.youtube.com/watch?v=" + video_id)


    internet_available()
    log(history, "CHECK_INTERNET")

    
    statrequest, exc = collect_stats(youtube, [video_id])
    if exc:
        log_error(history, exc, error=True)
        clear()

        return

    results = run(ryd([video_id]))

    log(history, "COLLECT_ONE_VIDEO_INFO", status="SUCCESS")
    clear()

    parsed_videos = output_videos(results, statrequest, one_video_info=True)
    log(history, "OUTPUT_ONE_VIDEO_INFO", status="SUCCESS")

    choice, full_path = save_docx(parsed_videos, keywords=video_id)
    log(history, "SAVE_DOCS", status="SUCCESS" if choice == "y" else "DECLINED", file_path=str(full_path) if choice == "y" else None)

    input("\nPress Enter to return...")
    log(history, "EXIT")