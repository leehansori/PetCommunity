from flask_request_validator.error_formatter import demo_error_formatter
from flask_request_validator.exceptions import InvalidRequestError

from pet_community.utils.response import request_validation_error
from pet_community.utils.response import error_response


def error_handle(app):
    """
    에러 핸들러
    Args:
        app  : __init__.py에서 파라미터로 app을 전달 받은 값
    Returns:
        json : error_response() 함수로 에러 메시지를 전달해서 반환 받고 return
    """

    @app.errorhandler(InvalidRequestError)
    def data_error(e):
        """
        validate_params 에러
        - null값 체크, rule(정규식,MaxLength 등) 검사
        """
        dev_error_message = request_validation_error(e)
        return error_response("입력값이 유효하지 않음", dev_error_message, 10)



