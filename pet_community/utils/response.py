import json

from flask import current_app
from flask_request_validator.validator import JSON, FORM, PATH, GET
from flask_request_validator.exceptions import *


def error_response(error_message, dev_error_message, status_code):
    """
    flask 는 기본 인코딩이 utf-8 이 아닌 ASCII 형태로 데이터를 출력
      -> [해결] 방법 중 하나, json.dumps(ensure_ascii=False)
    :param error_message: 사용자 에러 메시지
    :param dev_error_message: 개발자 에러 메시지
    :param status_code: 상태 코드
    :return:
    """

    result = {
        'code': status_code,
        'message': error_message
    }
    current_app.logger.debug(dev_error_message)

    return json.dumps(result, ensure_ascii=False)
# End of error_response


def request_validation_error(error: Union[InvalidRequestError]) -> dict:
    """
    validation error 로그 기록용 에러 메세지 출력
    """
    errors_by_type = {FORM: error.form, GET: error.get, JSON: error.json, PATH: error.path}

    sub_errors = {}
    for err_type, errors in errors_by_type.items():  # 에러 타입, 에러 내용
        if not errors:
            continue

        for err_key, sub_error in errors.items():
            if isinstance(sub_error, RequiredValueError):
                sub_errors[err_key] = "입력 값이 없습니다."
            if isinstance(sub_error, RulesError):
                sub_errors[err_key] = "유효한 값이 아닙니다."

    return sub_errors

