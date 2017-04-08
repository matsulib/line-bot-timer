## TIMER LINE BOT
入力された時間（秒）が経過したら通知してくれるLINE BOTです。

## Screenshot
![スクリーンショット](https://s3-ap-northeast-1.amazonaws.com/box-01/tmp/timer.PNG)

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
