# app/processor.py

from datetime import date
from loader import load_data
from db import connect_to_db, create_table, insert_data

def main():
    # Load data
    today = date.today()
    file_path = f"/data/{today.strftime('%Y-%m-%d')}.json"
    data = load_data(file_path)

    # Connect to MySQL database
    db = connect_to_db()
    cursor = db.cursor()

    # Create table if it doesn't exist
    create_table(cursor)

    # Insert data into the database
    insert_data(cursor, data)

    # Commit the transaction
    db.commit()

    # Close the database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
