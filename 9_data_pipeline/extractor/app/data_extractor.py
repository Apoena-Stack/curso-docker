import requests
from datetime import date
from config import API_URL
from date_utils import generate_date_range


def fetch_data_for_dates(start_date, end_date):

    dates = generate_date_range(start_date, end_date)
    data = []

    for d in dates:
        r = requests.get(f'{API_URL}{d}')

        r = r.json()

        intensity = r['data'][0]['intensity']
        forecast = intensity['forecast']
        actual = intensity['actual']
        index = intensity['index']
        
        data.append({
            "search_date": date.today().strftime("%Y-%m-%d"),
            "prevision_date": d,
            "index" : index,
            "actual": actual,
            "forecast": forecast
        })
    
    return data