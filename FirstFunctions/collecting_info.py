from googleapiclient.errors import HttpError

from Patterns.errors import PatternError, http_error, WinError





def channel_name(video_id, youtube):
    while True:
        try:
            name = youtube.videos().list(
                part="snippet",
                id=video_id
            ).execute()


            return name["items"][0]["snippet"]["channelId"], False
            

        except HttpError as exc:
            
            issue = http_error(exc)

            return issue, True
        

        except OSError as exc:

            if WinError(exc):
                continue

            return "OSError occurred", True
        
        except Exception:
            return PatternError().pattern_exception(), True
    


    
def collect_comments(video_id, search_terms, which_order, youtube):
    comments = []

    while True:
        try:
            while True:
                request = youtube.commentThreads().list(
                    part= "snippet,replies",
                    videoId= video_id,
                    maxResults= 100,
                    textFormat= "plainText",
                    order= which_order,
                ).execute()

                for item in request["items"]:

                    comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
                    if any(search_term.lower() in comment.lower() for search_term in search_terms):
                        comments.append(comment)

                    elif not search_terms:
                        comments.append(comment)
                        continue 

                    if "replies" in item:

                        for reply in item["replies"]["comments"]:
                            reply_comments = reply["snippet"]["textDisplay"]
                            
                            if any(reply_term.lower() in reply_comments.lower() for reply_term in search_terms):
                                comments.append(reply_comments)
                                
                            elif not search_terms:
                                comments.append(reply_comments)
                                continue

                comments = list(set(comments))


                return comments, False
        
        except HttpError as exc:
            return http_error(exc), True
        
        
        except OSError as exc:

            if WinError(exc):
                continue

            return "OSError occurred", True
        
        except Exception:
            return PatternError().pattern_exception(), True