from .auth import router as auth_router
from .filesystem import router as filesystem_router


def register_routes(app):
    app.register_blueprint(auth_router)
    app.register_blueprint(filesystem_router)
