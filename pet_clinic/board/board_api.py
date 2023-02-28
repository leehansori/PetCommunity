import json

from flask import Blueprint

board = Blueprint('board', __name__, url_prefix='/api/board')


# 게시판
# 로그인한 사용자는 게시판을 추가하고 관리한다.
# 게시물
# 사용자는 게시판에 게시물을 등록하고 관리한다.
# 댓글
# 사용자는 게시판에 다수의 댓글을 등록한다.
@board.route("/info", methods=['GET'])
def get_board_info() -> str:
    """
    게시판 목록 조회
    :return: 성공 시, 호스트 정보(호스트 ID, IP/PORT, 사용자 ID, 등록 일자/시간)
             실패 시, (30-DB 입력 오류)
    """
    try:
        board_manager = BoardManager()
        return json.dumps(host_manager.get_ht_info())
    except Exception as e:
        log.error(e)
        return json.dumps({'code': '30', 'message': 'DB 입력 오류'})
