import json
import unittest

import requests

"""
API 테스트(DB 연결 테스트)를 위한
unittest
"""


def response_print(url, response):
    print(f"url:{url}, response:{response}")
    if response.status_code == 200:
        print(json.loads(response.text))


class APITestCase(unittest.TestCase):

    def setUp(self):
        self.api_url = 'http://localhost:5000/api/'
        self.test_login()

    def test_rgst_mem(self):
        """
        회원 등록
        """
        body_data = {
            'id': 'aaa111@naver.com',
            'pw': 'Aaa111@',
            'name': '이한솔',
            'phone': '010-8812-4150'
        }
        print(body_data)

        url = self.api_url + 'member/register'
        response = requests.post(url, json=body_data)

        response_print(url, response)

    def test_check_pw(self):
        """
        비밀번호 확인
        """
        body_data = {
            'pw': 'Aaa111@',
            'check_pw': 'Aaa111@',
        }
        print(body_data)

        url = self.api_url + 'member/chkpw'
        response = requests.post(url, json=body_data)

        response_print(url, response)

    def test_login(self):
        """
        로그인
        """
        body_data = {
            'userID': 'aaa111@naver.com',
            'userPW': 'Aaa111@',
        }
        print(body_data)

        url = self.api_url + 'member/login'
        response = requests.post(url, json=body_data)

        response_print(url, response)

    def test_rgst_board(self):
        """
        게시판 등록
        """
        body_data = {
            'title': 'aaa111의 강아지 게시판',
        }
        print(body_data)

        url = self.api_url + 'board/register'
        response = requests.post(url, json=body_data)

        response_print(url, response)

    def test_board_list(self):
        """
        게시판 목록 조회
        """
        url = self.api_url + 'board/list'
        response = requests.get(url)

        response_print(url, response)

    def test_del_board(self, board_id=1):
        """
        게시판 삭제
        """
        url = self.api_url + 'board/' + str(board_id)
        response = requests.delete(url)

        response_print(url, response)

    def test_rgst_posting(self, board_id=1):
        """
        게시물 등록
        """
        body_data = {
            'title': '강아지 게시물1',
            'content': '강아지는 참 귀여워'

        }
        print(body_data)

        url = self.api_url + 'post/register/' + str(board_id)
        response = requests.post(url, json=body_data)

        response_print(url, response)

    def test_post_list(self, board_id=1):
        """
        게시물 목록 조회
        """
        url = self.api_url + 'post/list/' + str(board_id)
        response = requests.get(url)

        response_print(url, response)

    def test_mod_posting(self, posting_id=1):
        """
        게시물 수정
        """
        body_data = {
            'title': '강아지 게시물1 수정',
            'content': '수정 - 강아지는 참 귀여워'
        }
        print(body_data)

        url = self.api_url + 'post/' + str(posting_id)
        response = requests.put(url, json=body_data)

        response_print(url, response)

    def test_del_posting(self, posting_id=1):
        """
        게시물 삭제
        """
        url = self.api_url + 'post/' + str(posting_id)
        response = requests.delete(url)

        response_print(url, response)

    def test_rgst_reply(self, posting_id=1):
        """
        댓글 등록
        """
        body_data = {
            'content': '강아지 너무 귀엽네요'

        }
        print(body_data)

        url = self.api_url + 'reply/register/' + str(posting_id)
        response = requests.post(url, json=body_data)

        response_print(url, response)

    def test_reply_list(self, posting_id=1):
        """
        댓글 목록 조회
        """
        url = self.api_url + 'reply/list/' + str(posting_id)
        response = requests.get(url)

        response_print(url, response)

    def test_mod_reply(self, reply_id=1):
        """
        댓글 수정
        """
        body_data = {
            'content': '수정 - 강아지는 참 귀엽네요'
        }
        print(body_data)

        url = self.api_url + 'reply/' + str(reply_id)
        response = requests.put(url, json=body_data)

        response_print(url, response)

    def test_del_reply(self, reply_id=1):
        """
        댓글 삭제
        """
        url = self.api_url + 'reply/' + str(reply_id)
        response = requests.delete(url)

        response_print(url, response)


if __name__ == '__main__':
    unittest.main()
