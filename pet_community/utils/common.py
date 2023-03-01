import psycopg2
from psycopg2 import OperationalError, pool
import datetime as dt

from pet_community import config


def get_db_connection_pool():
    """
    PostgreSQL Connection Pool
    :return: conn_pool
    """
    conn_pool = None
    try:
        conn_pool = psycopg2.pool.SimpleConnectionPool(minconn=1, maxconn=20, user=config.DB_USERNAME,
                                                       password=config.DB_PASSWORD,
                                                       host=config.DB_HOST,
                                                       database=config.DB_NAME)
    except OperationalError as e:
        conn_pool = None
        raise e

    return conn_pool


def get_local_date_to_str() -> str:
    # 현재 날짜, 시간
    now = dt.datetime.now()
    # 형식 변경
    yyyymmdd = now.strftime("%Y%m%d")

    return yyyymmdd
