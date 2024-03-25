import mysql.connector
from mysql.connector import Error

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

# Execute SQL queries
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query Executed Successfully.")
    except Error as err:
        print(f"Error: '{err}'")

# Example usage:
if __name__ == "__main__":
    pw = 'Valerie'
    db = 'quiz'
    
    # Create quiz table query
    create_quiz_table = '''
    CREATE TABLE IF NOT EXISTS question (
        question_id INT PRIMARY KEY,
        question VARCHAR(1000) NOT NULL,
        option_1 VARCHAR(100) NOT NULL,
        option_2 VARCHAR(100) NOT NULL,
        option_3 VARCHAR(100) NOT NULL,
        option_4 VARCHAR(100) NOT NULL,
        answer VARCHAR(100) NOT NULL
    )
    '''
    
    # Create user table query
    create_user_table = '''
    CREATE TABLE IF NOT EXISTS users (
        user_id INT PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        score INT NOT NULL
    )
    '''
    
    # Create database connection
    connection = create_db_connection("localhost", "root", pw, db)
    
    # Execute queries
    execute_query(connection, create_quiz_table)
    execute_query(connection, create_user_table)
