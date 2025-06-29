import redis


POOL = redis.ConnectionPool(host='127.0.0.1', port=6379, encoding='utf-8', max_connections=100)
def push_queue(value):
    conn = redis.Redis(connection_pool=POOL)
    conn.lpush("DAY21_TASK_QUEUE", value)

def pop_queue():
    conn = redis.Redis(connection_pool=POOL)
    conn.rpop("spider_task_list")
