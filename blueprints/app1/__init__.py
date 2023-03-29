from posixpath import abspath
from flask import (
    Blueprint, request
)
from pprint import pprint
from utils import abspath
from utils.response_tools import ArgumentExceptionResponse, SuccessDataResponse
from utils.logger_tools import get_general_logger
import json

logger = get_general_logger(name='general', path=abspath('blueprints', 'app1', 'logs'))
bp = Blueprint('app1', __name__, url_prefix='/api/app1')


# functions for render responses for app1
@bp.route('', methods=['GET', 'POST'])
def render_response():
    pass
