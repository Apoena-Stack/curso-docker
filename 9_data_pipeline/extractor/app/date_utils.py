from datetime import timedelta


def generate_date_range(start_date, end_date):

    date_range = []
    current_date = start_date

    while current_date <= end_date:
        date_range.append(current_date.strftime("%Y-%m-%d"))
        current_date += timedelta(days=1)

    return date_range