from urllib.parse import urlencode
import random, string

from spotify.environ import CLIENT_ID, REDIRECT_URI


ENDPOINT = "https://accounts.spotify.com"

def url():
    random_string = "".join(random.choice(string.ascii_letters+string.digits) for _ in range(16))

    params = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "state": random_string,
        "scope": "user-read-playback-state user-read-recently-played user-top-read",
    }

    return ENDPOINT + "/authorize?" + urlencode(params)


if __name__ == "__main__":
    print(url())

