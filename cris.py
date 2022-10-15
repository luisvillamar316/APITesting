from flask import Flask, jsonify, abort, make_response, request
from flask import url_for
from markupsafe import escape

app = Flask(__name__)

playlists = [
    {
        "track": 1,
        "title": "Best Part",
        "artist": "Daniel Caesar",
        "done": False,
    },
    {
        "track": 2,
        "title": "Learn Python",
        "artist": "Need to find a good Python tutorial on the web",
        "done": False,
    },
]

@app.route('/')
def index():
    return "This is my assignment :) "
    
def make_public_playlist(playlist):
    new_playlist = {}
    for field in playlist:
        if field == "track":
            new_playlist["uri"] = url_for("get_playlist", playlist_track=playlist["track"], _external=True)
        else:
            new_playlist[field] = playlist[field]
    return new_playlist


@app.route("/myapitesting/api/v1.0/my_playlist", methods=["GET"])
#@auth.login_required()
def get_playlists():
    return jsonify({"playlists": [make_public_playlist(playlist) for playlist in playlists]})
    
@app.route("/myapitesting/api/v1.0/my_playlist/<int:playlist_track>", methods=["GET"])
def get_playlist(playlist_track):
    playlist = [playlist for playlist in playlists if playlist["track"] == playlist_track]
    if not playlist:
        abort(404)
    return jsonify(playlist)

@app.route("/myapitesting/api/v1.0/my_playlist", methods=["POST"])
def create_playlist():

    if not request.json or "title" not in request.json:
        abort(400)
    playlist = {
        "track": playlists[-1]["track"] + 1,
        "title": request.json["title"],
        "artist": request.json.get("artist", ""),
        "done": False,
    }
    playlists.append(playlist)
    return jsonify({"playlist": playlist}), 201


@app.route("/myapitesting/api/v1.0/my_playlist/<int:playlist_track>", methods=["PUT"])
def update_playlist(playlist_track):
    playlist = [playlist for playlist in playlists if playlist["track"] == playlist_track]
    if not playlist:
        abort(404)
    if not request.json:
        abort(400)
    if "title" in request.json and type(request.json["title"]) != str:
        abort(400)
    if "artist" in request.json and type(request.json["artist"]) is not str:
        abort(400)
    playlist[0]["title"] = request.json.get("title", playlist[0]["title"])
    playlist[0]["artist"] = request.json.get("artist", playlist[0]["artist"])
    playlist[0]["done"] = request.json.get("done", playlist[0]["done"])
    return jsonify({"playlist": playlist[0]})


@app.route("/myapitesting/api/v1.0/my_playlist/<int:playlist_track>", methods=["DELETE"])
def delete_playlist(playlist_track):
    playlist = [playlist for playlist in playlists if playlist["track"] == playlist_track]
    if not playlist:
        abort(404)
    playlists.remove(playlist[0])
    return jsonify({"result": True})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")