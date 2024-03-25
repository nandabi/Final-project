import mysql.connector
import sys

from mywork.homepage import home

# Database connection
def create_db_connection():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="ishwar",
            database="quiz"
        )
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        sys.exit(1)

# Run the program
if __name__ == "__main__":
    mydb = create_db_connection()
    mycursor = mydb.cursor()
    
    home()
