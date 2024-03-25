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
            host = host_name,
            user = user_name,
            passwd = user_password
        )
        print("Your server is running!!!")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

pw = 'ishwar'
db = 'quiz'

# Make connection
connection = create_server_connection("localhost", "root", pw)