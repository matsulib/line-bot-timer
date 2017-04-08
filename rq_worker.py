import os
import redis
from rq import Worker, Queue, Connection

import settings

listen = ['high', 'default', 'low']

conn = redis.from_url(settings.redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
