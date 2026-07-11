from datetime import datetime





def output_videos(results, statrequest, keywords=None, one_video_info=False):
    if not one_video_info:
        print(f"Your request: {keywords}")

    number = 0
    for item in statrequest["items"]:
        title = item["snippet"]["title"]
        video_id = item["id"]
        published_at = item["snippet"]["publishedAt"]
        dt = datetime.fromisoformat(published_at.replace("Z", "+00:00"))
        formatted_date = dt.strftime("%d.%m.%Y %H:%M:%S")

        likes = item["statistics"].get("likeCount", "No")
        dislikes = results.get(video_id, {}).get("dislikes", "No")
        views = item["statistics"].get("viewCount", "No")
        comments = item["statistics"].get("commentCount", "No")

        channelName = item["snippet"]["channelTitle"]
        channelId = item["snippet"]["channelId"]

        if one_video_info:
            description = item["snippet"]["description"]

        number += 1

        if not one_video_info:
            print(f"\n{number}.")
        print(
            f"Title: {title}\n"
            f"Video Link: https://www.youtube.com/watch?v={video_id}\n"
            f"{views} views; {likes} likes; {dislikes} dislikes; {comments} comments\n"
            f"Date: {formatted_date}\n"
            f"Channel: {channelName}\n"
            f"Channel URL: https://www.youtube.com/channel/{channelId}")
        if one_video_info:
            print(f"\nDescription:\n=================================\n{description}\n=================================")