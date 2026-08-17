from json import loads

from googleapiclient.errors import HttpError
from httplib2.error import ServerNotFoundError

from Patterns.check_connection import internet_available
from Patterns.errors import PatternError


def test_quota(youtube):
    while True:
        try:
            youtube.channels().list(
                part="snippet",
                id="UC0PhYO05DXdztwxvRSDfSiw"
            ).execute()
            return True


        except HttpError as exc:
            status = exc.resp.status
            
            if status == 403:
                error_reason = exc.content.decode("utf-8")
                error_json = loads(error_reason)
                reason = error_json["error"]["errors"][0]["reason"]

                if reason == "quotaExceeded":
                    print(f"\n\u001b[31mError {status}: Forbidden. You exceeded your YouTube API quota.\u001b[0m")

                else:
                    print(f"\n\u001b[31mUnexpected HTTP error: {status}\u001b[0m")

            return False
        
        except ServerNotFoundError:

            internet_available()

        except Exception as exc:
            PatternError().pattern_exception(exc)

            return False