import os
from pydub import AudioSegment
from pydub.playback import play

from flask import Flask, Response

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping()

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    @app.route("/wav")
    def stream_wav():
        def generate():
            with open("music.wav", "rb") as file:
                data = file.read(1024)
                while data:
                    yield data
                    data = file.read(1024)
        return Response(generate(), mimetype="audio/x-wav")


    return app