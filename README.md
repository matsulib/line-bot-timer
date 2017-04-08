## TIMER LINE BOT
入力された時間（秒）が経過したら通知してくれるLINE BOTです。

## Screenshot
![スクリーンショット](https://s3-ap-northeast-1.amazonaws.com/box-01/tmp/timer.PNG)

## 起動方法

以下の環境変数を設定
* LINE_CHANNEL_ACCESS_TOKEN
* LINE_CHANNEL_SECRET
* REDIS_HOST
* REDIS_PASSWORD
* REDIS_PORT

以下のプロセスを起動
* redis-server (ジョブキュー)
* python app.py (Webサーバ)
* python rq_worker.py (バックグラウンドワーカー)
* python timer_worker.py(バックグラウンドワーカー)

WebサーバはSSL通信が必須
