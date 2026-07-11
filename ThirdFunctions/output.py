from datetime import datetime

def output_channel_info(result, statrequests, get_answers, snistics, keywords=None):

    print(f"Channel: {snistics["title"]}\n"
          f"https://www.youtube.com/channel/{snistics["channelId"]}\n"
          f"CustomUrl: {snistics["customUrl"]}\n"
          f"Description:\n=================================\n{snistics["description"]}\n=================================\n"
          f"{snistics["subscriberCount"]} subs; {snistics["videoCount"]} videos; {snistics["viewCount"]} views.\n"
          f"Registration date: {snistics["publishedAt"]}\n")
    
    print("-" * 50)

    if get_answers == "y":
        print(f"Your request: {keywords}\n")
        print("Your received videos:")
        
    elif get_answers == "n":
        print("Four videos from the newest:")

    number = 0
    for item in statrequests["items"]:
        title_video = item["snippet"]["title"]
        videos_id = item["id"]
        vpublished_at = item["snippet"]["publishedAt"]
        dt = datetime.fromisoformat(vpublished_at.replace("Z", "+00:00"))
        vformatted_date = dt.strftime("%d.%m.%Y %H:%M:%S")

        ch_likes = item["statistics"].get("likeCount", "No")
        ch_dislikes = result.get(videos_id, {}).get("dislikes", "No")
        ch_views = item["statistics"].get("viewCount", "No")
        ch_comments = item["statistics"].get("commentCount", "No")

        number += 1

        print(
            f"\n{number}.\n"
            f"{title_video}\n"
            f"https://www.youtube.com/watch?v={videos_id}\n"
            f"{ch_views} views; {ch_likes} likes; {ch_dislikes} dislikes; {ch_comments} comments\n"
            f"{vformatted_date}")