from flask import Blueprint

router = Blueprint('files', __name__, url_prefix='/files')


@router.route("/")
def index():
    return "Files!!!"
