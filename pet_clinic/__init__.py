from flask import Flask

from pet_clinic.member import member_api
from pet_clinic.board import board_api


def create_app():
    app = Flask(__name__)

    app.register_blueprint(member_api.mem)
    app.register_blueprint(board_api.board)

    # error handler 등록
    # error_handle(app)

    return app

