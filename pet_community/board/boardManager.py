import psycopg2.extras

from pet_community.utils import common
from pet_community.utils.common import get_local_date_to_str

"""
 @author : Leehansol
 @title : 게시판 API에 해당하는 DB 수행 메소드 정의
"""


class BoardManager:

    user_id = None

    @staticmethod
    def get_board_list(id: str) -> dict:
        """
        DB에서 id에 해당하는 게시판 목록 정보를 가져오는 메소드
        :return: dict, 게시판 목록
        """

        conn_pool = common.get_db_connection_pool()

        try:
            with conn_pool.getconn() as conn:
                with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                    sql = "SELECT board_id, title FROM board WHERE id = %s and del_yn is not true " \
                          "order by regdate desc"

                    cur.execute(sql, [id])

                    board_lst = cur.fetchall()

        except Exception as e:
            raise e

        finally:
            if conn_pool and conn:
                conn.close()
                conn_pool.putconn(conn)
        return board_lst

    @staticmethod
    def insert_board(id: str, title) -> None:
        """
        DB에 게시판을 insert하는 메소드
        """

        conn_pool = common.get_db_connection_pool()

        try:
            with conn_pool.getconn() as conn:
                with conn.cursor() as cur:
                    insert_sql = """
                        INSERT INTO board (id, title, regdate)
                        VALUES(%s, %s, %s);
                    """

                    row = (id, title, get_local_date_to_str())

                    cur.execute(insert_sql, row)

                    conn.commit()

        except Exception as e:

            conn.rollback()  # 예외 발생시 rollback
            raise e

        finally:
            if conn_pool and conn:
                conn.close()
                conn_pool.putconn(conn)

    @staticmethod
    def delete_board(board_id: int) -> None:
        """
        DB에 게시판을 delete하는 메소드
        -> 데이터 보존을 위해 실제로 delete하지 않고
           del_yn 컬럼 true 변경
        """

        conn_pool = common.get_db_connection_pool()

        try:
            with conn_pool.getconn() as conn:
                with conn.cursor() as cur:
                    delete_rule_sql = """
                        update board 
                        set del_yn = true
                        where board_id = %s
                    """

                    cur.execute(delete_rule_sql, [board_id])
                    conn.commit()

        except Exception as e:

            conn.rollback()  # 예외 발생시 rollback
            raise e

        finally:
            if conn_pool and conn:
                conn.close()
                conn_pool.putconn(conn)

    @staticmethod
    def get_post_list(board_id: int) -> dict:
        """
        DB에서 board_id에 해당하는 게시물 목록 정보를 가져오는 메소드
        :return: dict, 게시판 목록
        """

        conn_pool = common.get_db_connection_pool()

        try:
            with conn_pool.getconn() as conn:
                with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                    sql = "SELECT title, content, regdate, updatedate FROM posting " \
                          "WHERE board_id = %s and del_yn is not true " \
                          "order by regdate desc"

                    cur.execute(sql, [board_id])

                    board_lst = cur.fetchall()

        except Exception as e:
            raise e

        finally:
            if conn_pool and conn:
                conn.close()
                conn_pool.putconn(conn)
        return board_lst

    @staticmethod
    def insert_posting(board_id: int, id: str, info: dict) -> None:
        """
        DB에 게시물을 insert하는 메소드
        """

        conn_pool = common.get_db_connection_pool()

        try:
            with conn_pool.getconn() as conn:
                with conn.cursor() as cur:
                    insert_sql = """
                            INSERT INTO posting (board_id, id, title, content, regdate)
                            VALUES(%s, %s, %s, %s, %s);
                        """

                    row = (board_id, id, info['title'],
                           info['content'], get_local_date_to_str())

                    cur.execute(insert_sql, row)

                    conn.commit()

        except Exception as e:

            conn.rollback()  # 예외 발생시 rollback
            raise e

        finally:
            if conn_pool and conn:
                conn.close()
                conn_pool.putconn(conn)

    @staticmethod
    def update_posting(posting_id: int, info: dict) -> None:
        """
        DB에 게시물을 update하는 메소드
        """

        conn_pool = common.get_db_connection_pool()

        try:
            with conn_pool.getconn() as conn:
                with conn.cursor() as cur:
                    update_img_sql = """
                                        update posting 
                                        set title = %s, content = %s, updatedate = %s
                                        where posting_id = %s
                                     """

                    row = (info['title'], info['content'], get_local_date_to_str(), posting_id)
                    cur.execute(update_img_sql, row)

                    conn.commit()

        except Exception as e:

            conn.rollback()  # 예외 발생시 rollback
            raise e

        finally:
            if conn_pool and conn:
                conn.close()
                conn_pool.putconn(conn)

    @staticmethod
    def delete_posting(posting_id: int) -> None:
        """
        DB에 게시물을 delete하는 메소드
        -> 데이터 보존을 위해 실제로 delete하지 않고
           del_yn 컬럼 true 변경
        """

        conn_pool = common.get_db_connection_pool()

        try:
            with conn_pool.getconn() as conn:
                with conn.cursor() as cur:
                    delete_rule_sql = """
                            update posting 
                            set del_yn = true
                            where posting_id = %s
                        """
                    cur.execute(delete_rule_sql, [posting_id])
                    conn.commit()

        except Exception as e:

            conn.rollback()  # 예외 발생시 rollback
            raise e

        finally:
            if conn_pool and conn:
                conn.close()
                conn_pool.putconn(conn)

    @staticmethod
    def get_reply_list(posting_id: int) -> dict:
        """
        DB에서 posting_id에 해당하는 댓글 목록 정보를 가져오는 메소드
        :return: dict, 게시판 목록
        """

        conn_pool = common.get_db_connection_pool()

        try:
            with conn_pool.getconn() as conn:
                with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                    sql = "SELECT id, content, regdate, updatedate FROM reply " \
                          "WHERE posting_id = %s order by regdate desc"

                    cur.execute(sql, [posting_id])

                    board_lst = cur.fetchall()

        except Exception as e:
            raise e

        finally:
            if conn_pool and conn:
                conn.close()
                conn_pool.putconn(conn)
        return board_lst
    @staticmethod
    def insert_reply(posting_id: int, id: str, info: dict) -> None:
        """
        DB에 댓글을 insert하는 메소드
        """

        conn_pool = common.get_db_connection_pool()

        try:
            with conn_pool.getconn() as conn:
                with conn.cursor() as cur:
                    insert_sql = """
                                INSERT INTO reply (posting_id, id, content, regdate)
                                VALUES(%s, %s, %s, %s);
                            """

                    row = (posting_id, id, info['content'], get_local_date_to_str())

                    cur.execute(insert_sql, row)

                    conn.commit()

        except Exception as e:

            conn.rollback()  # 예외 발생시 rollback
            raise e

        finally:
            if conn_pool and conn:
                conn.close()
                conn_pool.putconn(conn)

    @staticmethod
    def update_reply(reply_id: int, info: dict) -> None:
        """
        DB에 댓글을 update하는 메소드
        """

        conn_pool = common.get_db_connection_pool()

        try:
            with conn_pool.getconn() as conn:
                with conn.cursor() as cur:
                    update_img_sql = """
                        update reply 
                        set content = %s, updatedate = %s
                        where reply_id = %s
                     """

                    row = (info['content'], get_local_date_to_str(), reply_id)
                    cur.execute(update_img_sql, row)

                    conn.commit()

        except Exception as e:

            conn.rollback()  # 예외 발생시 rollback
            raise e

        finally:
            if conn_pool and conn:
                conn.close()
                conn_pool.putconn(conn)

    @staticmethod
    def delete_reply(reply_id: int) -> None:
        """
        DB에 댓글을 delete하는 메소드
        """

        conn_pool = common.get_db_connection_pool()

        try:
            with conn_pool.getconn() as conn:
                with conn.cursor() as cur:
                    delete_rule_sql = """ DELETE FROM reply WHERE reply_id = %s """

                    cur.execute(delete_rule_sql, [reply_id])
                    conn.commit()

        except Exception as e:

            conn.rollback()  # 예외 발생시 rollback
            raise e

        finally:
            if conn_pool and conn:
                conn.close()
                conn_pool.putconn(conn)

