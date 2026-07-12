from InputData.VideoExplorer import searching_for_videos

from SecondFunctions.collecting_info import collect_searches

from SecondFunctions.output import output_videos, save_docx

from Patterns.collectingStats import collect_stats

from Patterns.check_connection import internet_available

from Patterns.HistoryLogs import HistorySessions

from Patterns.save_history import log, log_error, clear

from Patterns.asyncRYD import ryd

from asyncio import run






def launcherVideos(youtube):
    history = HistorySessions("Video")

    keywords, region, ageAfter, ageBefore, duration, maximum, which_order, dimension = searching_for_videos()
    log(history, "ENTER_FILTER_SETTINGS", region=region, keywords=keywords, ageAfter=ageAfter, ageBefore=ageBefore,
        duration=duration, maximum=maximum, which_order=which_order, dimension=dimension)


    internet_available()
    log(history, "CHECK_INTERNET")

    
    video_ids, exc = collect_searches(youtube, keywords, region, ageAfter, ageBefore, duration, maximum, which_order, dimension)
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


    parsed_videos = output_videos(results, statrequest, keywords)
    log(history, "OUTPUT_VIDEOS", status="SUCCESS")
    

    choice, full_path = save_docx(parsed_videos, keywords, region)
    log(history, "SAVE_DOCS", status="SUCCESS" if choice == "y" else "DECLINED", file_path=str(full_path) if choice == "y" else None)


    input("\n\nPress Enter to return...")
    log(history, "EXIT")