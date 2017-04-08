#!/usr/bin/python3
import redis
from linebot.models import TextSendMessage

import settings

# LINE
line_bot_api = settings.line_bot_api

r = redis.from_url(settings.redis_url)
key_name = settings.timer_key_name


# textから待ち時間を特定する
def get_wait_time_sec(text):
    try:
        return int(text)
    except ValueError:
        return -1


# タイマーを設定する
def set_timer(message_id, sender_id, text, start_timestamp):
    wait_time_sec = get_wait_time_sec(text)
    if wait_time_sec < 0:
        line_bot_api.push_message(sender_id,
            TextSendMessage(text='error\U0001f635:{}\n id:{}\nInput a number.'.format(text, message_id)))
        return
    name = ':'.join([message_id, sender_id, text])
    end_timestamp = start_timestamp + wait_time_sec
    r.zadd(key_name, name, end_timestamp)
    line_bot_api.push_message(sender_id,
        TextSendMessage(text='processing:{}\n id:{}\nWaiting {} seconds...'.format(text, message_id, wait_time_sec)))