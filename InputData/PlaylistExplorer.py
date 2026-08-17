from re import search


def  playlist_URL_extract():
    playlist_URL = input('Enter the playlist URL with "PL" or "OL": ').strip()
    
    while True:
        playlist_URL = playlist_URL.strip()
        for_id = search(r"(PL[\w-]{32})", playlist_URL)
        if for_id:
            return for_id.group(1)
        
        playlist_URL = playlist_URL.strip()
        for_id = search(r"(OL[\w-]{39})", playlist_URL)
        if for_id:
            return for_id.group(1)

        playlist_URL = input("\nEnter again: ").strip()
