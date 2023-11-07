import os
from app import views
from flask import Flask

# Application factory
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
    
    return app

app = create_app()

app.add_url_rule('/', view_func=views.home)
app.add_url_rule("/files", view_func=views.getAudioFilesNames)
app.add_url_rule("/download", view_func=views.download)
app.add_url_rule("/play/<title>", view_func=views.play)
