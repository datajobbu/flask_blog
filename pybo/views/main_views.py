from flask import Blueprint


bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    return 'Pybo Index'


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'