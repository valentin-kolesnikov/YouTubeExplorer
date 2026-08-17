from googleapiclient.errors import HttpError

from Patterns.errors import PatternError, WinError, http_error


def collect_other_playlists(youtube, keywords, ageAfter, ageBefore, maximum, which_order):
    playlist_ids = []
    next_page_token = None

    while len(playlist_ids) < maximum:
        remaining_results = maximum - len(playlist_ids)
        current_max_results = min(remaining_results, 50)

        try:    
            request = youtube.search().list(
                q=keywords,
                publishedBefore=ageBefore,
                order=which_order,
                publishedAfter=ageAfter,
                part="snippet",
                type="playlist",
                maxResults=current_max_results,
                pageToken=next_page_token
            ).execute()

            for item in request["items"]:
                if "playlistId" in item["id"]:
                    playlist_ids.append(item["id"]["playlistId"])

            next_page_token = request.get("nextPageToken")

            if not next_page_token:
                break


        except HttpError as exc:
        
            issue = http_error(exc)

            return issue, True
        
        except OSError as exc:

            if WinError(exc):
                continue

            return "OSError occurred", True
        
        except Exception as exc:
            return PatternError().pattern_exception(exc), True
        
    return playlist_ids, False
    





def collect_playlist_details(youtube, playlist_ids):
    playlists = []

    for start in range(0, len(playlist_ids), 50):
        batch = playlist_ids[start:start + 50]

        while True:
            try:
                statrequest = youtube.playlists().list(
                    part="snippet,contentDetails,status",
                    id=",".join(batch)
                ).execute()

                playlists.extend(statrequest["items"])
                break
            
            except HttpError as exc:

                issue = http_error(exc)

                return issue, True
            
            except OSError as exc:

                if WinError(exc):
                    continue

                return "OSError occurred", True
            
            except Exception as exc:
                return PatternError().pattern_exception(exc), True

    return {"items": playlists}, False

    


def collect_videos_of_playlist(youtube, playlist_URL):
    video_ids = []
    next_page_token = None
    
    while True:
        try:
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

        except HttpError as exc:

            issue = http_error(exc)

            return issue, True
        
        except OSError as exc:

            if WinError(exc):
                continue

            return "OSError occurred", True
        
        except Exception as exc:
            return PatternError().pattern_exception(exc), True
    
    return video_ids, False



    

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