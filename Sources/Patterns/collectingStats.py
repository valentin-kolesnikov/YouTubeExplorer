from googleapiclient.errors import HttpError

from Patterns.errors import http_error, WinError








def collect_stats(youtube, video_ids):
    try:
        statrequest = youtube.videos().list(
            part="snippet,statistics",
            id=",".join(video_ids)
        ).execute()
        
        return statrequest, False
    
    
    except HttpError as exc:

        http_error(exc)

        return {}, True
    

    except Exception:
        print("Probably, YouTube has problems with submitted objects")

        return {}, True
        

    except OSError as exc:

        WinError(exc)

        return {}, True