import sys
import random
import mysql.connector
from mysql.connector import Error

import warnings
warnings.filterwarnings("ignore")

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("Your server is running!!!")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

pw = 'meyer'
db = 'quiz'

# Make connection
connection = create_server_connection("localhost", "root", pw)

# Database creation
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database Created Successfully.")
    except Error as err:
        print(f"Error: '{err}'")

create_database_query = "Create database quiz"
create_database(connection, create_database_query)

# database connection
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

# Execute sql queries
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query Executed Successful.")
    except Error as err:
        print(f"Error: '{err}'")

create_quiz_table = '''
create table question(
question_id int primary key,
question varchar(1000) not null,
option_1 varchar(100) not null,
option_2 varchar(100) not null,
option_3 varchar(100) not null,
option_4 varchar(100) not null,
answer varchar(100) not null
)
'''

connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, create_quiz_table)

create_user_table = '''
create table users(
user_id int primary key,
name varchar(50) not null,
score int not null
)
'''

connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, create_user_table)

# Question section
def Question():
    key = 'Y'
    
    while key == 'Y' or key == 'y':
        print("Welcome to Question Portal")
        print("***********************")
        question = input("Enter the question: ")
        option_1 = input("Enter the option 1: ")
        option_2 = input("Enter the option 2: ")
        option_3 = input("Enter the option 3: ")
        option_4 = input("Enter the option 4: ")
        answer = 0
        
        while answer == 0:
            option = int(input("Which option is correct answer (1,2,3,4): "))
            if option == 1:
                answer = option_1
            elif option == 2:
                answer = option_2
            elif option == 3:
                answer = option_3
            elif option == 4:
                answer = option_4
            else:
                print("Please choose the correct option as answer")
                
        mycursor.execute("Select * from question")
        data = mycursor.fetchall()
        question_id = (mycursor.rowcount) + 1
        mycursor.execute("Insert into question values (%s,%s,%s,%s,%s,%s,%s)",
                         (question_id, question, option_1, option_2, option_3, option_4, answer))
        mydb.commit()
        key = input("Question added successfully.. Do you want to add more (Y/N) ")
    Home()

# Quiz section
def Quiz():
    print("Welcome to Quiz portal")
    print("***********************")
    mycursor.execute("Select * from question")
    data = mycursor.fetchall()
    
    name = input("Enter your name: ")
    total_question = mycursor.rowcount
    to_attempt = int(input(f"Enter the number of questions to attempt (max {total_question}): "))
    
    question_ids = [i for i in range(1, total_question + 1)]
    question_ids = random.sample(question_ids, to_attempt)  # only some ids are required
   
    print("Quiz has started")
    c = 1
    score = 0
    for i in range(0, len(question_ids)):
        mycursor.execute("Select * from question where question_id=%s", (question_ids[i],))
        ques = mycursor.fetchone
