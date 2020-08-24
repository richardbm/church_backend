import arrow


def get_naive_datetime(date_time):
    return arrow.get(date_time).to('UTC').datetime.replace(tzinfo=None)
