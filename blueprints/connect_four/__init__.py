from posixpath import abspath
from flask import (
    Blueprint, request
)
from pprint import pprint
from utils import abspath
from utils.response_tools import ArgumentExceptionResponse, SuccessDataResponse
from utils.logger_tools import get_general_logger
# from utils.redis_tools import RedisWrapper, redis_cli

logger = get_general_logger(name='general', path=abspath('blueprints', 'connect_four', 'logs'))
bp = Blueprint('connect_four', __name__, url_prefix='/api/connect_four')


@bp.route('solution', methods=['GET'])
def get_solution():
    return "hello"

# @bp.route('symbols', methods=['GET'])
# def get_symbols():
#     stock_type = request.args.get('type', None)
#     if stock_type not in STOCK_TYPES:
#         return ArgumentExceptionResponse()
#
#     data = redis_cli.get('market_stock_list_a')
#     return SuccessDataResponse(data)
#
#
# @bp.route('indexs', methods=['GET'])
# def get_indexs():
#     stock_type = request.args.get('type', None)
#     if stock_type not in STOCK_TYPES:
#         return ArgumentExceptionResponse()
#
#     data = redis_cli.get('stock_index_list_a')
#     return SuccessDataResponse(data)
#
#
# @bp.route('concept_board', methods=['GET'])
# def get_concept_board():
#     data = redis_cli.get('concept_board_list_a')
#     return SuccessDataResponse(data)
#
#
# @bp.route('concept_member', methods=['GET'])
# def get_concept_member():
#     concept = request.args.get('concept', None)
#     if not concept:
#         return ArgumentExceptionResponse()
#
#     data = redis_cli.get(f'concept_member_list_a~{concept}')
#     return SuccessDataResponse(data)
#
#
# @bp.route('industry_board', methods=['GET'])
# def get_industry_board():
#     # keys = redis_cli.keys("*industry_board_list*")
#     # pprint(keys)
#
#     # data = redis_cli.get('industry_board_list')
#
#     r = RedisWrapper('local')
#     # keys = r.keys("*industry_board*")
#     # for key in keys:
#     #     pprint(r.get(key))
#
#     data = redis_cli.get('industry_board_list_a')
#     # data = redis_cli.get('industry_board_list_a')
#     pprint(type(data))
#     return SuccessDataResponse(data[:100])
#
#
# @bp.route('industry_member', methods=['GET'])
# def get_industry_member():
#     industry = request.args.get('industry', None)
#     if not industry:
#         return ArgumentExceptionResponse()
#
#     data = redis_cli.get(f'industry_member_list_a~{industry}')
#     return SuccessDataResponse(data)