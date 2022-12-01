from posixpath import abspath
from flask import (
    Blueprint, request
)
from pprint import pprint
from utils import abspath
from utils.response_tools import ArgumentExceptionResponse, SuccessDataResponse
from utils.logger_tools import get_general_logger
# from utils.redis_tools import RedisWrapper, redis_cli
from strategy.maxmin_alpha_pruning_connect4 import MaxMin
from tools.connect_four_board_decode import decode_connect_four
import json

logger = get_general_logger(name='general', path=abspath('blueprints', 'connect_four', 'logs'))
bp = Blueprint('connect_four', __name__, url_prefix='/api/connect_four')


@bp.route('solution', methods=['GET', 'POST'])
def get_solution():

    try:
        data = json.loads(request.json)
        method = data["method"]
        board = data["board"]
        number_to_win = data["connectNumber"]

    except:
        return ArgumentExceptionResponse()

    try:
        if method == "maxmin":
            game_board = decode_connect_four(board)
            game = MaxMin()
            game.runMinMax(game_board, 8, number_to_win=number_to_win, http=True)
            data = game.output + 1
            return SuccessDataResponse(data)
    except:
        return ArgumentExceptionResponse()
