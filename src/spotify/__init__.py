import requests
import spotify.accesstoken
from spotify.classes import Track, Album, Artist, Image


ENDPOINT = 'https://api.spotify.com/v1'


def getRecentlyPlayedTracks():
    '''
    Get user's recently playes tracks.

    Returns
    -------
    res : list(dict(Track, str))
        List with Track objects and the played time.

    See Also
    --------
    getTopTracks()
    getTopArtists()
    '''

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + spotify.accesstoken.get()
    }

    params = {
        "limit": 50
    }

    res = requests.get(ENDPOINT + '/me/player/recently-played', headers=headers, params=params)
    res.raise_for_status()

    res_dict = res.json()

    data = []
    for item in res_dict["items"]:
        track = item["track"]

        album = track["album"]
        album = Album(
            id=album["id"],
            name=album["name"],
            artists=[Artist(id=artist["id"], name=artist["name"], href=artist["external_urls"]["spotify"]) for artist in album["artists"]],
            href=album["external_urls"]["spotify"],
            images=[Image(width=image["width"], height=image["height"], url=image["url"]) for image in album["images"]],
            release_date=album["release_date"],
            total_tracks=album["total_tracks"]
        )
        
        artists = track["artists"]
        artists = [Artist(
            id=artist["id"], 
            name=artist["name"], 
            href=artist["external_urls"]["spotify"],
        ) for artist in artists]

        track = Track(
            id=track["id"],
            name=track["name"],
            album=album,
            artists=artists,
            href=track["external_urls"]["spotify"],
            explicit=track["explicit"],
            popularity=track["popularity"],
            preview_url=track["preview_url"],
        )
        data.append({
            "data": track,
            "played_at": item["played_at"]
        })

    return data


def getTopArtists(time_range: str = "short_term"):
    '''
    Get user's top artists.

    Parameters
    ----------
    time_range : str
        Over what time frame the affinities are computed. 
        Valid values: 
            long_term (several years), 
            medium_term (approximately last 6 months), 
            short_term (approximately last 4 weeks). 
        Default: short_term

    Returns
    -------
    res : list(Artist)
        List with Artist objects.

    See Also
    --------
    getTopTracks()
    getRecentlyPlayedTracks()
    '''

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + spotify.accesstoken.get()
    }

    params = {
        "limit": 50
    }

    res = requests.get(ENDPOINT + f'/me/top/artists?time_range={time_range}', headers=headers, params=params)
    res.raise_for_status()

    res_dict = res.json()

    data = []
    for item in res_dict["items"]:
        artist = Artist(
            id=item["id"], 
            name=item["name"], 
            href=item["external_urls"]["spotify"],
            popularity=item["popularity"],
            images=[Image(width=image["width"], height=image["height"], url=image["url"]) for image in item["images"]],
            followers=item["followers"]["total"],
            genres=item["genres"],
        )
        
        data.append(artist)

    return data


def getTopTracks(time_range: str = "short_term"):
    '''
    Get user's top tracks.

    Parameters
    ----------
    time_range : str
        Over what time frame the affinities are computed. 
        Valid values: 
            long_term (several years), 
            medium_term (approximately last 6 months), 
            short_term (approximately last 4 weeks). 
        Default: short_term

    Returns
    -------
    res : list(Track)
        List with Track objects.

    See Also
    --------
    getTopArtists()
    getRecentlyPlayedTracks()
    '''

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + spotify.accesstoken.get()
    }

    params = {
        "limit": 50
    }

    res = requests.get(ENDPOINT + f'/me/top/tracks?time_range={time_range}', headers=headers, params=params)
    res.raise_for_status()

    res_dict = res.json()

    data = []
    for item in res_dict["items"]:
        album = item["album"]
        album = Album(
            id=album["id"],
            name=album["name"],
            artists=[Artist(id=artist["id"], name=artist["name"], href=artist["external_urls"]["spotify"]) for artist in album["artists"]],
            href=album["external_urls"]["spotify"],
            images=[Image(width=image["width"], height=image["height"], url=image["url"]) for image in album["images"]],
            release_date=album["release_date"],
            total_tracks=album["total_tracks"]
        )
        
        artists = item["artists"]
        artists = [Artist(
            id=artist["id"], 
            name=artist["name"], 
            href=artist["external_urls"]["spotify"],
        ) for artist in artists]

        track = Track(
            id=item["id"],
            name=item["name"],
            album=album,
            artists=artists,
            href=item["external_urls"]["spotify"],
            explicit=item["explicit"],
            popularity=item["popularity"],
            preview_url=item["preview_url"],
        )
        data.append(track)

    return data

