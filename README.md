# Spotify Statistics Website

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3107/)

Combining the Spotify API with Flask, this project lets a user connect to their Spotify account and get lists of their recent activities and data. My focus was the backend and not the frontend - which is quite simple.\
Please [Notice](#notice).

<br/>

# Table of contents
- [Installation](#installation)
- [Usage](#usage)
- [Notice](#notice)

<br/>

# Installation

<details>
<summary>1. Clone this repository</summary>
<p>

```sh
git clone https://github.com/dnellessen/spotify-stats.git
```

</p>
</details>

<details>
<summary>2. Install all required python libraries</summary>
<p>

```sh
pip install -r requirements.txt
```

</p>
</details>

<br/>

# Usage

Go the the [Spotify for Developers](https://developer.spotify.com/dashboard/login) website, login to your account and create a new app. In its overview edit the settings and add a redirect URI (e.g. http://127.0.0.1:8000/callback). Important: Make sure the path is ```/callback```. I'd suggest using your local host. \
Now add the following environment variables (ajust according to the host and port your are using and make sure they are equivalent to those you just set as a redirect URI):
```sh
export CLIENT_ID='Your Client ID'
export CLIENT_SECRET='Your Client Secret'
export SERVER_HOST='127.0.0.1'
export SERVER_PORT='8000'
```
Great, everything should be set up. Now you can start the server with:
```sh 
python3 src/server.py
```
Authenticate and you should see three tables with the following data:
- Recently Played
- Top Tracks [4 weeks]
- Top Artists [4 weeks]

<br/>

# Notice

This is a very simple example of how to use the Spotify API and show the data to a user. However, it is not developement friendly as it is not build correctly for that purpose. Use and expand this project for yourself to learn and enjoy.
