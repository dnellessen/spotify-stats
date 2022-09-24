from dataclasses import dataclass

@dataclass
class Image:
    width: int
    height: int
    url: str


@dataclass
class Album:
    id: str
    name: str
    artists: list
    href: str
    images: list
    release_date: str
    total_tracks: int


@dataclass
class Artist:
    id: str
    name: str
    href: str
    popularity: int = None
    images: list = None
    followers: int = None
    genres: list = None


@dataclass
class Track:
    id: str
    name: str
    album: Album
    artists: list
    href: str
    explicit: bool
    popularity: int
    preview_url: str

