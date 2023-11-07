from flask import make_response, request, render_template
from pytube import YouTube
from lib import file


def home():
    return render_template("/partials/home.html")

def getAudioFilesNames():
    print("Called get audio files")
    audioFiles = file.read_files("/files")
    print(audioFiles)
    response = make_response(
            render_template("partials/audio.html",
                navigation=audioFiles),
        )
    response.headers["Content-Type"] = "application/json"
    response.status = 200
    return response

def download():
    yt_link = request.args.get("link")
    yt = YouTube(yt_link)
    stream = yt.streams.get_by_itag(140)
    stream.download(output_path="./files", filename="1.mp4")

    response = make_response("ok")
    return response

def play(title):
    normal_title = file.normalize(title)
    def generate():
        with open(f"./files/{normal_title}", "rb") as file:
            data = file.read(1024)
            while data:
                yield data
                data = file.read(1024)

    response = make_response(generate())
    response.mimetype = "audio/mp4"
    return response