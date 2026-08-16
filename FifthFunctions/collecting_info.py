from youtube_transcript_api._errors import (
    NoTranscriptFound,
    TranslationLanguageNotAvailable,
    VideoUnavailable,
)

from Patterns.errors import PatternError
from Patterns.save_history import log


def transcript_fetcher(history, video_id_list, languages_list, manually_generated):
    try:
        if manually_generated == "1":
            transcript_subtitles = video_id_list.find_manually_created_transcript(languages_list)

        elif manually_generated == "2":
            transcript_subtitles = video_id_list.find_generated_transcript(languages_list)

        return transcript_subtitles, False
    
    
    except NoTranscriptFound:
        log(history, "NO_TRANSCRIPT_FOUND_FIRST_ATTEMPT")

        try:
            if manually_generated == "1":
                generated_forced = input("\nThere is no manually created transcript. Do you try to find a generated transcript?\n\n" \
                "1. Yes\n2. No\n\nEnter the number: ").strip()

                while True:

                    if generated_forced == "1":
                        transcript_subtitles = video_id_list.find_generated_transcript(languages_list)
                        break

                    elif generated_forced == "2":
                        log(history, "EXIT", reason="User declined to search for generated transcript")
                        return {}, True
                    
                    else:
                        generated_forced = input("Enter again: ").strip()


            elif manually_generated == "2":

                manually_forced = input("There is no generated transcript. Do you try to find a manually created transcript?\n\n" \
                "1. Yes\n2. No\n\nEnter the number: ").strip()

                while True:

                    if manually_forced == "1":
                        transcript_subtitles = video_id_list.find_manually_created_transcript(languages_list)
                        break

                    elif manually_forced == "2":
                        log(history, "EXIT", reason="User declined to search for manually created transcript")
                        return {}, True
                    
                    else:
                        manually_forced = input("Enter again: ").strip()
                

            return transcript_subtitles, False
        
        
        except NoTranscriptFound:

            input("\n\u001b[31mNo transcripts were found\u001b[0m\n\nPress Enter to return...")
            log(history, "NO_TRANSCRIPT_FOUND_LAST_ATTEMPT")

            return {}, True
    

    except VideoUnavailable:

        input("\u001b[31mThe video is unavailable\u001b[0m\n\nPress Enter to return...")
        log(history, "VIDEO_UNAVAILABLE")

        return {}, True
    
    except TranslationLanguageNotAvailable:

        input("\u001b[31mThe translation language is not available\u001b[0m\n\nPress Enter to return...")
        log(history, "TRANSLATION_LANGUAGE_NOT_AVAILABLE")

        return {}, True
    
    except Exception as exc:
        PatternError().pattern_exception(exc), True

        return {}, True