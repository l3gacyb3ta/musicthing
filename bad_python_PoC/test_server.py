from bottle import template, run, post,route, request, static_file, response, get
from uuid import uuid4
database = {}

@route("/<artistname>/<album>/buy")
def buy(artistname: str, album: str) -> dict:
    sessionid = uuid4().__str__()
    database[sessionid] = { # track whether user has paid
        "status": "not confirmed",
        "music": {
            "artist": artistname,
            "album": album
        },
    }

    return {
        "payment": {
            "processor": "stripe",
            "url": "/test_buy_url"
        },
        "music": {
            "artist": artistname,
            "album": album
        },
        "sessionid": sessionid
    }

@post("/test_buy_url")
def test_buy():
    """A super simple "payment processor" that just requires you to send your session id"""
    data = request.json
    if isinstance(data, dict):
        database[data["sessionid"]]["status"] = "confirmed"
    
@get("/<artistname>/<album>/deliver")
def deliver(artistname: str, album: str):
    """Only delivers content (a random png) if you've confirmed"""
    data = request.json
    if isinstance(data, dict):
        if database[data["sessionid"]]["status"] == "confirmed":
            return static_file("image-1.png", "../design")
        else:
            response.status = 403 

run()