from googleapiclient.errors import HttpError

from Patterns.errors import PatternError, WinError, http_error


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

            playlist_ids = [item["id"]["playlistId"] for item in request["items"]]

            return playlist_ids, False


        except HttpError as exc:
        
            issue = http_error(exc)

            return issue, True
        
        except OSError as exc:

            if WinError(exc):
                continue

            return "OSError occurred", True
        
        except Exception as exc:
            return PatternError().pattern_exception(exc), True
    





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
        
        except Exception as exc:
            return PatternError().pattern_exception(exc), True
    


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

                video_ids.extend(
                    item["contentDetails"]["videoId"] for item in playlist_request["items"]
                )

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
        
        except Exception as exc:
            return PatternError().pattern_exception(exc), True



    

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

                statrequest.extend(mine_playlists["items"])

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
        
        except Exception as exc:
            return PatternError().pattern_exception(exc), True