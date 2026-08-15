from Starter.KeyExplorer import memory


def launcherKey(exc_OAuth2):
    key = memory.load_key()
    if key:
        print(f"YouTube API key: {key}\n")
    else:
        print("No YouTube API key\n")

    if not exc_OAuth2:
        print("Remember! You are using OAuth2. If you want to use API key, delete the token files and restart the program.")

    input("\nPress Enter to return...")