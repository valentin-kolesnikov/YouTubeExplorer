from googleapiclient.errors import HttpError

from Patterns.errors import http_error, WinError








def collect_stats(youtube, video_ids):
    try:
        statrequest = youtube.videos().list(
            part="snippet,statistics",
            id=video_ids
        ).execute()
        
        dict_channels = {}
        
        for stat in statrequest["items"]:
            channelName = stat["snippet"]["channelTitle"]
            channelId = stat["snippet"]["channelId"]

        dict_channels["Name"] = channelName
        dict_channels["Id"] = channelId
        
        return statrequest, dict_channels, False
    
    except HttpError as exc:

        http_error(exc)

        return {}, {}, True
    

    except Exception:
        print("Probably, YouTube has problems with submitted objects")

        return {}, {}, True
        

    except OSError as exc:

        WinError(exc)

        return {}, {}, True           #перезагрузка программы