from tkinter.messagebox import QUESTION
import mysql.connector
import sys

from mywork.quizsec import quiz

# Database connection
def create_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="yourdatabase"
    )

# Create home page
def home():
    while True:
        print("Welcome to Quiz")
        print("********************")
        print("1. Enter Questions")
        print("2. Take Quiz")
        print("3. Exit")
        opt = int(input("Enter your choice: "))

        if opt == 1:
            QUESTION()
        elif opt == 2:
            quiz ( )
        elif opt == 3:
            print("Exiting the Quiz")
            sys.exit()
        else:
            print("Invalid choice. Please select again.")

