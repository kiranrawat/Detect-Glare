import datetime

class UtcDateTimeUtils():
    def fetch_utc_datetime(self, epoch):
        """
        This function takes epoch as an input and convert it to UTC standard
        parameter ---
        epoch : Linux epoch in second
        """
        try:
            return datetime.datetime.utcfromtimestamp(epoch)
        except Exception as e:
            raise e