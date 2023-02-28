import json

from flask import Blueprint
from flask_request_validator import validate_params, Param, JSON, Pattern

mem = Blueprint('mem', __name__, url_prefix='/api/member')


# 회원 가입 : 중복 확인
# 회원 정보 수정
# 로그인

@mem.route("/register", methods=['POST'])
@validate_params(
    Param('user_id', JSON, str, rules=[Pattern(r'^[a-zA-Z0-9]+$')], required=True),  # 대소문자와 숫자만 가능
    Param('ht_ip', JSON, str, rules=[Pattern(r'(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9]['
                                             r'0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$')], required=True),  # IPv4
    Param('ht_port', JSON, str, rules=[Pattern(r'^[0-9]{1,5}$')], required=True)  # 포트 번호: 길이 최대 5, 숫자만 가능
)
def reg_mem_info():
    """
    회원 정보 등록
    :return: 등록 결과 (00-성공, 10-입력값이 유효하지 않음, 30-DB 입력 오류, 42-이미 등록된 호스트 존재)
    """

    return json.dumps({'code': '00', 'message': '성공'})
