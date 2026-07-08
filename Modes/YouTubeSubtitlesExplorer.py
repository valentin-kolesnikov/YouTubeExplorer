from youtube_transcript_api import YouTubeTranscriptApi

from youtube_transcript_api._errors import (VideoUnplayable, RequestBlocked, TranscriptsDisabled)

from Patterns.EnteringURL import youtube_id_finder

from Patterns.HistoryLogs import HistorySessions

from Patterns.save_history import log, log_error, clear

from Patterns.errors import WinError

from FifthFunctions.collecting_info import transcript_fetcher

from FifthFunctions.output import available_languages, transcript_fetch, output, save_docx

from InputData.SubtitlesExplorer import language_needed, view_of_text











def launcherSubtitles():
    history = HistorySessions("Subtitles")

    video_id = youtube_id_finder()
    log(history, "ENTER_VIDEO_LINK", video_link="https://www.youtube.com/watch?v=" + video_id)
    
    while True:
        try:
            video_list = YouTubeTranscriptApi().list(video_id)
            break

        except OSError as exc:

            if WinError(exc):
                continue

            log(history, "OSError occurred", error=str(exc))
            return
        
        except VideoUnplayable:

            input("\n\u001b[31mThe video is unplayable\u001b[0m\n\nPress Enter to return...")
            log(history, "VIDEO_UNPLAYABLE")

            return
        
        except RequestBlocked:

            input("\n\u001b[31mYouTube is blocking requests from your IP\u001b[0m\n\nPress Enter to return...")
            log(history, "REQUEST_BLOCKED")

            return
        
        except TranscriptsDisabled:

            input("\n\u001b[31mThe video does not have subtitles\u001b[0m\n\nPress Enter to return...")
            log(history, "TRANSCRIPTS_DISABLED")

            return
    

    languages_list = language_needed()
    log(history, "ENTER_LANGUAGES", languages=languages_list)

    manually_generated = view_of_text()
    log(history, "ENTER_VIEW", view="Manually created" if manually_generated == "1" else "Generated")

    transcript_subtitles, exc = transcript_fetcher(history, video_list, languages_list, manually_generated)
    if exc:
        clear()
        return
    log(history, "FIND_TRANSCRIPT", status="SUCCESS")

    
    while True:
        try:
            available_lang = available_languages(transcript_subtitles)

            full_text = transcript_fetch(transcript_subtitles)

            break

        except OSError as exc:

            if WinError(exc):
                continue

            log(history, "OSError occurred", error=str(exc))
            return
    

    clear()

    output(transcript_subtitles, available_lang, full_text)
    log(history, "OUTPUT_TRANSCRIPT", status="SUCCESS", available_languages=available_lang)


    choice, full_path = save_docx(transcript_subtitles, available_lang, full_text)
    log(history, "SAVE_DOCS", status="SUCCESS" if choice == "y" else "DECLINED", file_path=str(full_path) if choice == "y" else None)


    input("\n\nPress Enter to return...")
    log(history, "EXIT")