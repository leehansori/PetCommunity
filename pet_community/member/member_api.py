import json
import re

from flask import Blueprint, current_app, request
from flask_login import login_user, logout_user, current_user
from flask_request_validator import validate_params, Param, JSON, Pattern, ValidRequest, MaxLength
from werkzeug.security import generate_password_hash

from pet_community.member.memManager import MemManager, User
from pet_community.board.boardManager import BoardManager

"""
 @author : Leehansol
 @title : 회원 API
"""

# blueprint 등록
mem = Blueprint('mem', __name__, url_prefix='/member')
app = Blueprint('app', __name__, url_prefix='/')


@mem.route("/register", methods=['POST'])
@validate_params(
    # id : 이메일 형식
    Param('id', JSON, str, rules=[Pattern(r'^[a-zA-Z0-9+-\_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')], required=True, ),
    # 비밀번호 형식 : 최소 한개의 영문자 + 최소 한개의 숫자 + 최소 한개의 특수 문자
    Param('pw', JSON, str, required=True,
          rules=[Pattern(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]'), MaxLength(50)]),
    Param('name', JSON, str, rules=[MaxLength(50)], required=True),
    Param('phone', JSON, str, rules=[Pattern(r'(010|019|011)-\d{4}-\d{4}')], required=False),
    Param('regdate', JSON, str, required=True)
)
def reg_mem_info(valid: ValidRequest):
    """
    회원 정보 등록
    :return: 등록 결과 (00-성공, 10-입력값이 유효하지 않음, 20-이미 존재하는 id입니다.)
    """

    # receive json data
    mem_info = valid.get_json()
    id = mem_info.get('id')

    # 핸드폰 번호에서 특수기호 지움
    phone = re.sub(r"[^0-9]", "", mem_info.get('phone'))

    # id 중복 확인
    try:
        id_count = MemManager.check_id(id)
        if id_count > 0:
            return json.dumps({'code': '20', 'message': '이미 존재하는 id입니다.'})
    except Exception as e:
        current_app.logger.error(e)

    # DB 입력
    try:
        # DB 입력 값 정의
        info = {'id': id,
                'pw': generate_password_hash(mem_info.get('pw')),
                'name': mem_info.get('name'),
                'phone': phone,
                'regdate': mem_info.get('regdate')}

        # DB insert
        MemManager.insert_mem(info)

    except Exception as e:
        current_app.logger.error(e)
        return json.dumps({'code': '30', 'message': 'DB 입력 오류'})

    return json.dumps({'code': '00', 'message': '성공'})


@mem.route("/chkpw", methods=['POST'])
@validate_params(
    # 비밀번호 형식 : 최소 한개의 영문자 + 최소 한개의 숫자 + 최소 한개의 특수 문자
    Param('pw', JSON, str, required=True,
          rules=[Pattern(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]'), MaxLength(50)]),
    Param('check_pw', JSON, str, required=True,
          rules=[Pattern(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]'), MaxLength(50)])
)
def check_pw(valid: ValidRequest):
    """
    비밀번호 확인
    :return: 등록 결과 (00-성공, 10-입력값이 유효하지 않음, 20-비밀번호가 일치하지 않습니다.)
    """

    # receive json data
    pw_info = valid.get_json()

    if pw_info.get('pw') != pw_info.get('check_pw'):
        return json.dumps({'code': '20', 'message': '비밀번호가 일치하지 않습니다.'})

    return json.dumps({'code': '00', 'message': '성공'})


@mem.route('/login', methods=['GET', 'POST'])
def login():
    """
    로그인
    :return: 등록 결과 (00-로그인 성공, 10-ID,PW를 입력해주세요, 20-일치하는 회원 정보가 없습니다.)
    """

    # json 데이터를 가져옴
    info = request.get_json()
    # id, pw 가져옴
    user_id = info.get('userID')
    user_pw = generate_password_hash(info.get('userPW'))

    # 사용자가 입력한 정보가 회원가입된 사용자인지 확인
    user_info = User.get_user_info(user_id, user_pw)

    if user_info == 0:
        # 사용자 객체 생성
        login_info = User(user_id=user_id)
        # 사용자 객체를 session에 저장
        login_user(login_info)
        BoardManager.user_id = current_user.user_id
    else:
        return json.dumps({'code': '20', 'message': '일치하는 회원 정보가 없습니다.'})

    return json.dumps({'code': '00', 'message': '로그인 성공'})


@mem.route('/logout')
def logout():
    """
    로그아웃
    :return: 등록 결과 (00-로그아웃 성공)
    """
    # session 정보를 삭제
    logout_user()
    return json.dumps({'code': '00', 'message': '로그아웃 성공'})

