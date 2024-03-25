import mysql.connector
from mysql.connector import Error

# Database creation
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database Created Successfully.")
    except Error as err:
        print(f"Error: '{err}'")

# Database connection
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database Connection Successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

# Example usage:
if __name__ == "__main__":
    pw = 'Valerie'
    db = 'quiz'
    
    # Create database
    create_database_query = "CREATE DATABASE IF NOT EXISTS quiz"
    connection = create_db_connection("localhost", "root", pw, "")
    create_database(connection, create_database_query)
    
    # Connect to database
    connection = create_db_connection("localhost", "root", pw, db)
