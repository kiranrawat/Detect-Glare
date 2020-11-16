import datetime


class UtcDateTimeUtils():
     # convert the epoch to utc datetime
    def fetch_utc_datetime(self, epoch):
        try:
            return datetime.datetime.utcfromtimestamp(epoch)
        except Exception as e:
            raise e