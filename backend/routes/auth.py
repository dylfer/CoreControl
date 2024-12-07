from flask import Blueprint

router = Blueprint('auth', __name__, url_prefix='/auth')


@router.post("/login")
def login():
    return "test"


@router.post("/signup")
def signup():
    return ""
