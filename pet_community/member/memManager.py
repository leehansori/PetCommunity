from pet_community.utils import common
from pet_community.utils.common import get_local_date_to_str

from flask_login import UserMixin

"""
 @author : Leehansol
 @title : 회원 API에 해당하는 DB 수행 메소드 정의
"""


class User(UserMixin):
    """
    flask-login session
    """

    def __init__(self, user_id):
        self.user_id = user_id

    def get_id(self):
        return str(self.user_id)

    @staticmethod
    def get_user_info(user_id: str, user_pw: str) -> int:
        """
        DB에서 동일한 id,pw가 존재 하는지 확인
        :param user_pw:
        :param user_id:
        :return int, 일치하는 id 수
        """
        conn_pool = common.get_db_connection_pool()

        try:
            with conn_pool.getconn() as conn:
                with conn.cursor() as cur:
                    get_count_sql = """ SELECT COUNT(*) FROM member WHERE id = %s and pw = %s"""
                    row = (user_id, user_pw)
                    cur.execute(get_count_sql, row)
                    count = cur.fetchone()[0]

        except Exception as e:
            raise e

        finally:
            if conn_pool and conn:
                conn.close()
                conn_pool.putconn(conn)
        return count


class MemManager:

    @staticmethod
    def check_id(id: str) -> int:
        """
        DB에서 동일한 id가 존재 하는지 확인
        :param id
        :return int, 동일한 id 수
        """

        conn_pool = common.get_db_connection_pool()

        try:
            with conn_pool.getconn() as conn:
                with conn.cursor() as cur:
                    get_count_sql = """ SELECT COUNT(*) FROM member WHERE id = %s """
                    cur.execute(get_count_sql, [id])
                    count = cur.fetchone()[0]

        except Exception as e:
            raise e

        finally:
            if conn_pool and conn:
                conn.close()
                conn_pool.putconn(conn)
        return count

    @staticmethod
    def insert_mem(info: dict) -> None:
        """
        DB에 회원 정보를 insert하는 메소드
        """

        conn_pool = common.get_db_connection_pool()

        try:
            with conn_pool.getconn() as conn:
                with conn.cursor() as cur:
                    insert_sql = """
                        INSERT INTO member (id, pw, name, phone, regdate)
                        VALUES(%s, %s, %s, %s, %s);
                    """

                    row = (info['id'], info['pw'],
                           info['name'], info['phone'], get_local_date_to_str())

                    cur.execute(insert_sql, row)

                    conn.commit()

        except Exception as e:

            conn.rollback()  # 예외 발생시 rollback
            raise e

        finally:
            if conn_pool and conn:
                conn.close()
                conn_pool.putconn(conn)

