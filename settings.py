#!/usr/bin/python3
import os
from linebot import (
    LineBotApi, WebhookHandler
)


# LINE
line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET'))

# redis
redis_host = os.getenv('REDIS_HOST')
redis_port = os.getenv('REDIS_PORT')
redis_password = os.getenv('REDIS_PASSWORD')

# timer
timer_key_name = 'timer'
timer_interval_sec = 1