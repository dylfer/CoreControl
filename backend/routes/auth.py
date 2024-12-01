from flask import Blueprint

router = Blueprint('auth', __name__, url_prefix='/auth')


@router.route("/login")
def login():
    return ""


@router.route("/signup")
def signup():
    return ""
