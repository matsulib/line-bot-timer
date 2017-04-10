from pytz import timezone
from datetime import datetime


utc_tz = timezone('UTC')
jst_tz = timezone('Asia/Tokyo')
format = '%Y-%m-%d %H:%M:%S'


def timestamp2jst_str(timestamp):
    return datetime.fromtimestamp(timestamp, utc_tz).astimezone(jst_tz).strftime(format)
