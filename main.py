from backend.routes import register_routes
from react import start_nextjs_dev_server
from flask import Flask
import json


app = Flask(__name__, static_folder='public', static_url_path='/')

clients = {}


register_routes(app)


if __name__ == '__main__':
    # checks
    # start_nextjs_dev_server()
    # main run
    app.run(port=8000, debug=True)
