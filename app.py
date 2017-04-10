#!/usr/bin/python3
import os
from datetime import datetime
from pytz import timezone
from rq import Queue
from flask import (
    Flask, request, abort
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)

import settings
from rq_worker import conn
from line_jobs import set_timer
from jstutil import timestamp2jst_str


# LINE
line_bot_api = settings.line_bot_api
handler = settings.handler

app = Flask(__name__)


@app.route('/callback', methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info('Request body: ' + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 受信メッセージ
    text = event.message.text
    # メッセージID
    message_id = event.message.id
    # 送信者ID
    sender_id = event.source.sender_id
    # タイムスタンプ
    timestamp = int(str(event.timestamp)[:10])
    # とりあえず返信
    start_datetime = timestamp2jst_str(timestamp)
    line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text='begin:{}\n id:{}\n{}'.format(text, message_id, start_datetime)))

    # 処理をキューに登録して非同期で実行
    q = Queue(connection=conn)
    q.enqueue(set_timer, message_id, sender_id, text, timestamp)


@handler.default()
def default(event):
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text='\U0001f604'))


if __name__ == '__main__':
    port = int(os.getenv('PORT', '5001'))
    host = os.getenv('HOST', 'localhost')

    app.run(host=host, port=port, threaded=True, debug=True)

