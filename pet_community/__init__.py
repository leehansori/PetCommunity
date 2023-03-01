import os

from flask import Flask
from flask_login import LoginManager
import logging
from logging.handlers import RotatingFileHandler

from pet_community.member import member_api
from pet_community.board import board_api
from pet_community.utils.error_handler import error_handle


def create_app():
    app = Flask(__name__)

    # blueprint 등록
    app.register_blueprint(member_api.mem)
    app.register_blueprint(board_api.board)
    app.register_blueprint(board_api.post)
    app.register_blueprint(board_api.reply)
    app.register_blueprint(member_api.app)

    # flask log-in
    login_manager = LoginManager()
    login_manager.init_app(app)
    app.secret_key = os.urandom(24)

    # 로그 설정
    if not app.debug:
        # 파일에 저장 (정해진 사이즈를 넘어가면 새로운 파일에 저장)
        file_handler = RotatingFileHandler(
            './pet_community.log',  # 파일 이름 (경로 포함)
            encoding='utf-8',
            maxBytes=(1024 * 1024 * 1),  # 하나의 파일 사이즈 (현재 1 MB)
            backupCount=10  # 파일 갯수
        )
        file_handler.setFormatter(
            logging.Formatter('[%(asctime)s] %(levelname)s in %(filename)s>%(funcName)s(%(''lineno)s): ''%(message)s'))
        app.logger.setLevel(logging.DEBUG)
        # file_handler 등록
        app.logger.addHandler(file_handler)

    # error handler 등록
    # validate_params 에러 등을 체크하기 위해 따로 정의
    error_handle(app)

    return app

