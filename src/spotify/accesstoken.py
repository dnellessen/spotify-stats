from base64 import b64encode
import requests
import os
import json
import time

from spotify.environ import CLIENT_SECRET, CLIENT_ID, REDIRECT_URI


ENDPOINT = "https://accounts.spotify.com"
PATH = os.path.dirname(__file__)


def get() -> str:
    '''
    Get access token from saved file.
    If the token has expired, it gets refreshed and returned.

    Returns
    -------
    token : str

    See Also
    --------
    request()   
    '''

    with open(f"{PATH}/token.json", 'r') as file:
        token_dict = json.load(file)

    if token_dict["expires_at"] > time.time():
        return token_dict['access_token']
    refresh(token_dict["refresh_token"])
    return get()


def refresh(refresh_token: str) -> None:
    '''
    Refresh access token.

    Parameters
    ----------
    refresh_token : str
        The refresh token returned from the authorization code exchange.

    See Also
    --------
    get()   
    '''

    url = ENDPOINT + "/api/token"

    params = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
    }

    headers = {
        "Authorization": "Basic " + b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode(),
        "Content-Type": "application/x-www-form-urlencoded",
    }

    res = requests.post(url, params=params, headers=headers)
    res.raise_for_status()

    __write2file(res)


def request(code: str) -> None:
    '''
    Request access token from Spotify API.

    Parameters
    ----------
    code : str
        The code from the redirect url.

    See Also
    --------
    get()   
    '''

    url = ENDPOINT + "/api/token"

    params = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
    }

    headers = {
        "Authorization": "Basic " + b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode(),
        "Content-Type": "application/x-www-form-urlencoded",
    }

    res = requests.post(url, params=params, headers=headers)
    res.raise_for_status()

    __write2file(res)


def __write2file(res):
    '''
    Writes Spotify API response to JSON file.

    Parameters
    ----------
    res : Response
        The response from the POST request.
    '''

    token_dict = res.json()
    token_dict["expires_at"] = token_dict["expires_in"] + time.time()

    with open(f"{PATH}/token.json", 'w') as file:
        file.write(json.dumps(token_dict))

