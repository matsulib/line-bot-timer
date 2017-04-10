## TIMER LINE BOT
入力された時間（秒）が経過したら通知してくれるLINE BOTです。

## Screenshot
![スクリーンショット](https://qiita-image-store.s3.amazonaws.com/0/141719/f71142be-7dd7-9393-c800-cc54bb48efad.png)

## 起動方法
環境変数を設定
* LINE_CHANNEL_ACCESS_TOKEN
* LINE_CHANNEL_SECRET

heroku add-on
* Redis To Go

```
$ heroku addons:create redistogo
$ git push heroku master
$ heroku ps:scale rq_worker=1 timer_worker=1
```
