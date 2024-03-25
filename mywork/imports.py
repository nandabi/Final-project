import mysql.connector

# Establish a connection to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

# Create a cursor object
mycursor = mydb.cursor()

# Now you can use mycursor to execute SQL queries
mycursor.execute("SELECT * FROM your_table")

# Fetch and print the results, for example:
for row in mycursor.fetchall():
    print(row)

# Don't forget to close the cursor and connection when done
mycursor.close()
mydb.close()