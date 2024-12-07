from flask import Flask, request, jsonify
from .auth import router as auth_router
from .filesystem import router as filesystem_router


def register_routes(app):

    @app.before_request
    def before_request():
        # list of paths that don't require authentication
        if not request.path.startswith("/auth/"):
            return  # jsonify({'error': 'you naughty boy'}), 401

    app.register_blueprint(auth_router)
    app.register_blueprint(filesystem_router)
