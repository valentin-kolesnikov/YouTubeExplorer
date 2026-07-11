from json import loads

class PatternError:
    def pattern_exception():
        print("Probably, YouTube has problems with submitted objects")

        return "Unexpected error occurred" 


def http_error(exc):
    status = exc.resp.status

    match status:
        case 400:
            issue = "Bad Request. There are some issues with Google requests. Make sure that you entered correctly."

        case 403:
            error_json = loads(exc.content.decode("utf-8"))
            reason = error_json["error"]["errors"][0]["reason"]

            if reason == "commentsDisabled":
                issue = "Forbidden. Comments of the video are disabled."
            else:
                issue = "Forbidden. Probably, you exceeded your YouTube API quota."

        case 404:
            issue = "Not Found. Probably, the requested video does not exist."

        case _:
            issue = "Unexpected HTTP error"

    print(f"\n\u001b[31mError {status}: {issue}\u001b[0m")
    

    input("\nPress Enter to return...")

    return issue






def WinError(exc):

    match exc.errno:
        case 10054:
            issue = "Connection was forcibly closed by the remote host (WinError 10054)"

        case 11001:
            issue = "No Internet connection available (WinError 11001)"

        case _:
            issue = "Internet connection is probably unavailable."

    print(f"\n\u001b[31m{issue}\u001b[0m")


    exit_continue = input("\n\u001b[31m1. Retry connection\n2. Exit\n\nYour choice:\u001b[0m").strip()
    
    while True:
        if exit_continue == "1":
            return True
        
        elif exit_continue == "2":
            exit(1)

        else:
            exit_continue = input("\n\u001b[31mEnter again:\u001b[0m").strip()