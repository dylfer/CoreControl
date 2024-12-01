from react import start_nextjs_dev_server
from flask import Flask, request, jsonify, send_file

from backend.routes import register_routes

app = Flask(__name__, static_folder='public', static_url_path='/')

register_routes(app)

if __name__ == '__main__':
    # checks
    # start_nextjs_dev_server()
    # main run
    app.run(port=3000, debug=True)
