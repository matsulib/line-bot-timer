import os
import redis
from rq import Worker, Queue, Connection

import settings

listen = ['high', 'default', 'low']

conn = redis.Redis(host=settings.redis_host, port=settings.redis_port, password=settings.redis_password)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
