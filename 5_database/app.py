import mysql.connector
from mysql.connector import Error

def create_connection(host, user, password, db):
    
    connection = None
    try:
        connection = mysql.connector.connect(

            host=host,
            user=user,
            passwd=password,
            database=db

        )

        print("Conexão Estabelecida.")
    except Error as e:
        print("Erro na conexão",e)

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()

    cursor.execute(query)
    connection.commit()

    print("Query executada.")

def main():

    connection = create_connection("localhost","root","passwordroot","mysqldb")

    create_table = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT,
        name TEXT NOT NULL,
        age INT,
        PRIMARY KEY (id)
    ) ENGINE = InnoDB
    """

    execute_query(connection, create_table)

    insert_query = """
    INSERT INTO users (name, age)
    VALUES ('John Doe', 28)
    """

    execute_query(connection, insert_query)

    select_users = "SELECT * FROM users"

    cursor = connection.cursor()
    cursor.execute(select_users)

    users = cursor.fetchall()

    for user in users:
        print(user)

if __name__ == "__main__":
    main()