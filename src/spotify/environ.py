import os

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REDIRECT_URI = "http://" + os.environ.get("SERVER_HOST") + ":" + os.environ.get("SERVER_PORT") + "/callback"
