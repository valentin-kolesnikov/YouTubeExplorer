from googleapiclient.errors import HttpError

from Patterns.errors import PatternError, http_error, WinError








def collect_other_playlists(youtube, keywords, ageAfter, ageBefore, maximum, which_order):
    while True:
        try:
            request = youtube.search().list(
                q=keywords,
                publishedBefore=ageBefore,
                order=which_order,
                publishedAfter=ageAfter,
                part="snippet",
                type="playlist",
                maxResults=maximum,
            ).execute()

            playlist_ids = []

            for item in request["items"]:
                playlist_id = item["id"]["playlistId"]
                playlist_ids.append(playlist_id)

            return playlist_ids, False


        except HttpError as exc:
            
            http_error(exc)
            
            return {}, True
        
        
        except OSError as exc:

            if WinError(exc):
                continue

            return {}, True
        
        except Exception:
            
            print("Probably, YouTube has problems with submitted objects")

            return {}, True
    





def collect_playlist_details(youtube, playlist_ids):
    while True:
        try:
            statrequest = youtube.playlists().list(
                part="snippet,contentDetails,status",
                id=",".join(playlist_ids)
            ).execute()

            return statrequest, False
        
        
        except HttpError as exc:

            issue = http_error(exc)

            return issue, True
        
        except OSError as exc:

            if WinError(exc):
                continue

            return "OSError occurred", True
        
        except Exception:
            return PatternError().pattern_exception(), True
    


def collect_videos_of_playlist(youtube, playlist_URL):
    while True:
        try:
            video_ids = []
            next_page_token = None

            while True:
                playlist_request = youtube.playlistItems().list(
                    part="contentDetails",
                    playlistId=playlist_URL,
                    maxResults=50,
                    pageToken=next_page_token
                ).execute()

                for item in playlist_request["items"]:
                    video_ids.append(item["contentDetails"]["videoId"])

                next_page_token = playlist_request.get("nextPageToken")

                if not next_page_token:
                    break

            return video_ids, False


        except HttpError as exc:

            issue = http_error(exc)

            return issue, True
        
        except OSError as exc:

            if WinError(exc):
                continue

            return "OSError occurred", True
        
        except Exception:
            return PatternError().pattern_exception(), True



    

def collect_your_playlists(youtube):
    while True:
        try:
            statrequest = []
            next_page_token = None

            while True:
                mine_playlists = youtube.playlists().list(
                    part="snippet,contentDetails,status",
                    maxResults=50,
                    pageToken=next_page_token,
                    mine=True
                ).execute()

                for item in mine_playlists["items"]:
                    statrequest.append(item)

                next_page_token = mine_playlists.get("nextPageToken")

                if not next_page_token:
                    break

            return {"items": statrequest}, False

        except HttpError as exc:

            issue = http_error(exc)

            return issue, True
        
        except OSError as exc:

            if WinError(exc):
                continue

            return "OSError occurred", True
        
        except Exception:
            return PatternError().pattern_exception(), True