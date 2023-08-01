"""
This module defines a flask app and registers blueprint
It serves at HNBN_API_HOST or 0.0.0.0, port HNBN_API_PORT or 5000
"""
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def purge_session(req):
    storage.close()


if __name__ == "__main__":
    from os import getenv

    host = getenv("HNBN_API_HOST", "0.0.0.0")
    port = getenv("HNBN_API_PORT", "5000")
    app.run(host=host, port=port, threaded=True)