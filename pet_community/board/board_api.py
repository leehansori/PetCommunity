import json

from flask import Blueprint, current_app
from flask_request_validator import validate_params, Param, JSON, Pattern, ValidRequest, MaxLength

from pet_community.board.boardManager import BoardManager

"""
 @author : Leehansol
 @title : 게시판 관련 API
"""

# blueprint 등록
board = Blueprint('board', __name__, url_prefix='/api/board')
post = Blueprint('post', __name__, url_prefix='/api/post')
reply = Blueprint('reply', __name__, url_prefix='/api/reply')


@board.route("/list", methods=['GET'])
def get_board_list() -> str:
    """
    user_id의 게시판 목록 조회
    :return: 성공 시, 게시판 목록
             실패 시, (30-DB 오류, 40-로그인을 해주세요)
    """
    if BoardManager.user_id is None:
        return json.dumps({'code': '40', 'message': '로그인을 해주세요.'})

    try:
        board_list = BoardManager.get_board_list(BoardManager.user_id)
    except Exception as e:
        current_app.logger.error(e)
        return json.dumps({'code': '30', 'message': 'DB 조회 오류'})

    return json.dumps(board_list)


@board.route("/register", methods=['POST'])
@validate_params(
    Param('title', JSON, str, rules=[MaxLength(50)], required=True),
)
def register_board(valid: ValidRequest) -> str:
    """
    게시판 추가
    :return: 성공 시, (00-성공)
             실패 시, (30-DB 오류, 40-로그인을 해주세요)
    """
    # receive json data
    info = valid.get_json()

    if BoardManager.user_id is None:
        return json.dumps({'code': '40', 'message': '로그인을 해주세요.'})

    # DB 입력
    try:
        BoardManager.insert_board(BoardManager.user_id, info.get("title"))
        current_app.logger.debug(f"게시판 등록(DB) - id:{BoardManager.user_id} ")
    except Exception as e:
        current_app.logger.error(e)
        return json.dumps({'code': '30', 'message': 'DB 입력 오류'})

    return json.dumps({'code': '00', 'message': '성공'})


@board.route('/<int:board_id>', methods=['DELETE'])
def del_board(board_id) -> str:
    """
    게시판 삭제
    :return: 성공 시, (00-성공)
             실패 시, (30-DB 오류, 40-로그인을 해주세요)
    """

    if BoardManager.user_id is None:
        return json.dumps({'code': '40', 'message': '로그인을 해주세요.'})

    # DB 삭제
    try:
        BoardManager.delete_board(board_id)
        current_app.logger.debug(f"게시판 삭제(DB) - board_id:{board_id} ")
    except Exception as e:
        current_app.logger.error(e)
        return json.dumps({'code': '30', 'message': 'DB 삭제 오류'})

    return json.dumps({'code': '00', 'message': '성공'})


# 게시물 관련 --------------
@post.route("/list/<int:board_id>", methods=['GET'])
def get_post_list(board_id) -> str:
    """
    user_id의 게시물 목록 조회
    :return: 성공 시, 게시판 목록
             실패 시, (30-DB 오류, 40-로그인을 해주세요)
    """
    if BoardManager.user_id is None:
        return json.dumps({'code': '40', 'message': '로그인을 해주세요.'})

    try:
        post_list = BoardManager.get_post_list(board_id)
    except Exception as e:
        current_app.logger.error(e)
        return json.dumps({'code': '30', 'message': 'DB 조회 오류'})

    return json.dumps(post_list)


@post.route("/register/<int:board_id>", methods=['POST'])
@validate_params(
    Param('title', JSON, str, rules=[MaxLength(50)], required=True),
    Param('content', JSON, str, required=True),
)
def register_posting(valid: ValidRequest, board_id) -> str:
    """
    게시물 추가
    :return: 성공 시, (00-성공)
             실패 시, (30-DB 조회 오류, 40-로그인을 해주세요)
    """
    # receive json data
    post_info = valid.get_json()

    if BoardManager.user_id is None:
        return json.dumps({'code': '40', 'message': '로그인을 해주세요.'})

    # DB 입력
    try:
        # DB 입력 값 정의
        info = {'title': post_info.get('title'),
                'content': post_info.get('content')}
        # DB 입력
        BoardManager.insert_posting(board_id, BoardManager.user_id, info)
        current_app.logger.debug(f"게시물 등록(DB) - id:{BoardManager.user_id} ")
    except Exception as e:
        current_app.logger.error(e)
        return json.dumps({'code': '30', 'message': 'DB 입력 오류'})

    return json.dumps({'code': '00', 'message': '성공'})


@post.route("/<int:posting_id>", methods=['PUT'])
@validate_params(
    Param('title', JSON, str, rules=[MaxLength(50)], required=True),
    Param('content', JSON, str, required=True),
)
def update_posting(valid: ValidRequest, posting_id) -> str:
    """
    게시물 수정
    :return: 성공 시, (00-성공)
             실패 시, (30-DB 조회 오류, 40-로그인을 해주세요)
    """
    # receive json data
    post_info = valid.get_json()

    if BoardManager.user_id is None:
        return json.dumps({'code': '40', 'message': '로그인을 해주세요.'})

    # DB 입력
    try:
        # DB 수정 값 정의
        info = {'title': post_info.get('title'),
                'content': post_info.get('content')}
        # DB 수정
        BoardManager.update_posting(posting_id, info)
        current_app.logger.debug(f"게시물 수정(DB) - posting_id:{posting_id} ")

    except Exception as e:
        current_app.logger.error(e)
        return json.dumps({'code': '30', 'message': 'DB 입력 오류'})

    return json.dumps({'code': '00', 'message': '성공'})


@post.route('/<int:posting_id>', methods=['DELETE'])
def del_posting(posting_id) -> str:
    """
    게시물 삭제
    :return: 성공 시, (00-성공)
             실패 시, (30-DB 오류, 40-로그인을 해주세요)
    """

    if BoardManager.user_id is None:
        return json.dumps({'code': '40', 'message': '로그인을 해주세요.'})

    # DB 삭제
    try:
        BoardManager.delete_posting(posting_id)
        current_app.logger.debug(f"게시물 삭제(DB) - posting_id:{posting_id} ")
    except Exception as e:
        current_app.logger.error(e)
        return json.dumps({'code': '30', 'message': 'DB 삭제 오류'})

    return json.dumps({'code': '00', 'message': '성공'})


# 댓글 관련 --------------
@reply.route("/list/<int:posting_id>", methods=['GET'])
def get_reply_list(posting_id: int) -> str:
    """
    posting_id의 게시물 목록 조회
    :param: 댓글을 조회할 게시물의 posting_id
    :return: 성공 시, 댓글 목록
             실패 시, (30-DB 오류, 40-로그인을 해주세요)
    """
    if BoardManager.user_id is None:
        return json.dumps({'code': '40', 'message': '로그인을 해주세요.'})

    try:
        post_list = BoardManager.get_reply_list(posting_id)
    except Exception as e:
        current_app.logger.error(e)
        return json.dumps({'code': '30', 'message': 'DB 조회 오류'})

    return json.dumps(post_list)


@reply.route("/register/<int:posting_id>", methods=['POST'])
@validate_params(
    Param('content', JSON, str, required=True),
)
def register_reply(valid: ValidRequest, posting_id) -> str:
    """
    댓글 추가
    :return: 성공 시, (00-성공)
             실패 시, (30-DB 조회 오류, 40-로그인을 해주세요)
    """
    # receive json data
    reply_info = valid.get_json()

    if BoardManager.user_id is None:
        return json.dumps({'code': '40', 'message': '로그인을 해주세요.'})

    # DB 입력
    try:
        # DB 입력 값 정의
        info = {'content': reply_info.get('content')}
        # DB 입력
        BoardManager.insert_reply(posting_id, BoardManager.user_id, info)
        current_app.logger.debug(f"댓글 등록(DB) - posting_id:{posting_id} ")

    except Exception as e:
        current_app.logger.error(e)
        return json.dumps({'code': '30', 'message': 'DB 입력 오류'})

    return json.dumps({'code': '00', 'message': '성공'})


@reply.route("/<int:reply_id>", methods=['PUT'])
@validate_params(
    Param('content', JSON, str, required=True),
)
def update_reply(valid: ValidRequest, reply_id) -> str:
    """
    댓글 수정
    :return: 성공 시, (00-성공)
             실패 시, (30-DB 조회 오류, 40-로그인을 해주세요)
    """
    # receive json data
    reply_info = valid.get_json()

    if BoardManager.user_id is None:
        return json.dumps({'code': '40', 'message': '로그인을 해주세요.'})

    # DB 입력
    try:
        # DB 수정 값 정의
        info = {'content': reply_info.get('content')}
        # DB 수정
        BoardManager.update_reply(reply_id, info)
        current_app.logger.debug(f"댓글 수정(DB) - reply_id:{reply_id} ")

    except Exception as e:
        current_app.logger.error(e)
        return json.dumps({'code': '30', 'message': 'DB 입력 오류'})

    return json.dumps({'code': '00', 'message': '성공'})


@reply.route('/<int:reply_id>', methods=['DELETE'])
def del_reply(reply_id) -> str:
    """
    댓글 삭제
    :return: 성공 시, (00-성공)
             실패 시, (30-DB 오류, 40-로그인을 해주세요)
    """

    if BoardManager.user_id is None:
        return json.dumps({'code': '40', 'message': '로그인을 해주세요.'})

    # DB 삭제
    try:
        BoardManager.delete_reply(reply_id)
        current_app.logger.debug(f"댓글 삭제(DB) - reply_id:{reply_id} ")
    except Exception as e:
        current_app.logger.error(e)
        return json.dumps({'code': '30', 'message': 'DB 삭제 오류'})

    return json.dumps({'code': '00', 'message': '성공'})