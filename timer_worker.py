import time
import asyncio
import redis
from datetime import datetime
from linebot.models import TextSendMessage

import settings

# LINE
line_bot_api = settings.line_bot_api

r = redis.from_url(settings.redis_url)
key_name = settings.timer_key_name


async def timer(delay):
    while True:
        now = time.time()
        for name, end_timestamp in r.zrange(key_name, 0, -1, withscores=True):
            diff = end_timestamp - now
            if diff <= 0:
                message_id, sender_id, text = name.decode().split(':')
                end_datetime = datetime.fromtimestamp(int(now))
                line_bot_api.push_message(sender_id,
                    TextSendMessage(text='end:{}\n id:{}\n{}'.format(text, message_id, end_datetime)))
                r.zrem(key_name, name)
            else:
                break
        await asyncio.sleep(delay)


if __name__ == '__main__':
    r.flushall()
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(timer(1))
    finally:
        loop.close()
