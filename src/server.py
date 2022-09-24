from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap

import spotify
import spotify.authorize
import spotify.accesstoken
import os


app = Flask(__name__)
Bootstrap(app)

HOST = os.environ.get("SERVER_HOST")
PORT = int(os.environ.get("SERVER_PORT"))

authorized = False


@app.get("/")
def home():
    if not authorized:
        return render_template("connect.html")
    return render_template(
        "home.html", 
        top_tracks=spotify.getTopTracks(),
        top_artists=spotify.getTopArtists(),
        recently_played=spotify.getRecentlyPlayedTracks()
    )


@app.get("/authorize")
def authorize():
    return redirect(spotify.authorize.url())


@app.get("/callback")
def callback():
    global authorized
    code = request.args.get("code")
    spotify.accesstoken.request(code)
    authorized = True
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(HOST, PORT, debug=True)

