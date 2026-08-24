from googleapiclient.errors import HttpError

from Patterns.errors import PatternError, WinError, http_error


def collect_stats(youtube, video_ids):
    while True:
        try:
            statrequest = []

            for i in range(0, len(video_ids), 50):

                statrequest_videos = youtube.videos().list(
                    part="snippet,statistics",
                    id=",".join(video_ids[i:i+50])
                ).execute()

                statrequest.extend(statrequest_videos["items"])
            
        
        
        except HttpError as exc:
            error = http_error(exc)
            break
        
        except OSError as exc:

            if WinError(exc):
                continue

            error = "OSError occurred"
            break
        
        except Exception as exc:
            error = PatternError().pattern_exception(exc)
            break

    return {"items": statrequest}, error