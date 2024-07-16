from datetime import date, timedelta
from data_extractor import fetch_data_for_dates
from file_writer import save_data_to_file


def main():

    today = date.today()
    start_date = today - timedelta(days=1)
    end_date = today + timedelta(days=1)


    data = fetch_data_for_dates(start_date, end_date)
    save_data_to_file(data)



if __name__ == "__main__":
    main()