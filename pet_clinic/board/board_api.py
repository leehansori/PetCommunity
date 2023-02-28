from flask import Blueprint

board = Blueprint('board', __name__, url_prefix='/api/board')


# 게시판
# 로그인한 사용자는 게시판을 추가하고 관리한다.
# 게시물
# 사용자는 게시판에 게시물을 등록하고 관리한다.
# 댓글
# 사용자는 게시판에 다수의 댓글을 등록한다.
@board.route("/hello", methods=['GET'])
def hello():
    return "hello world"
