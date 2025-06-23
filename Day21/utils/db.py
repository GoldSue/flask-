import pymysql
from dbutils.pooled_db import PooledDB
from pymysql import cursors
# 初始化连接池
POOL = PooledDB(
    creator=pymysql,          # 指定数据库驱动模块
    maxconnections=10,        # 连接池最大连接数
    mincached=2,              # 初始化时，连接池中至少创建的空闲连接
    maxcached=3,              # 连接池中最多空闲连接数
    blocking=True,            # 连接池中如果没有可用连接后，是否阻塞等待
    setsession=[],            # 开始会话前执行的命令列表
    ping=1,                   # 检查连接是否可用的方式，1 表示每次执行查询前检查
    host='127.0.0.1',
    port=3306,
    user='root',
    password='Gold7789@',
    charset='utf8mb4',        # 建议使用 utf8mb4 支持更多字符
    db='flask'
)


def fetch_one(sql, params=None):
    """执行查询并返回一条结果"""
    with POOL.connection() as conn:
        with conn.cursor(cursor=cursors.DictCursor) as cursor:
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            result = cursor.fetchone()
    return result


def fetch_all(sql, params=None):
    with POOL.connection() as conn:
        with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            result = cursor.fetchall()
    return result


def get_current_db():
    with POOL.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT DATABASE()")
            db_name = cursor.fetchone()
    print("当前数据库:", db_name)
    return db_name

get_current_db()


