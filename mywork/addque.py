import mysql.connector

from mywork.homepage import home

def add_question():
    mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="yourdatabase"
    )
    mycursor = mydb.cursor()

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
            option = int(input("Which option is the correct answer (1, 2, 3, 4): "))
            if option == 1:
                answer = option_1
            elif option == 2:
                answer = option_2
            elif option == 3:
                answer = option_3
            elif option == 4:
                answer = option_4
            else:
                print("Please choose a correct option as the answer")
                
        mycursor.execute("SELECT * FROM question")
        data = mycursor.fetchall()
        question_id = len(data) + 1
        
        sql = "INSERT INTO question (question_id, question, option_1, option_2, option_3, option_4, answer) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (question_id, question, option_1, option_2, option_3, option_4, answer)
        
        mycursor.execute(sql, val)
        mydb.commit()
        
        print("Question added successfully.")
        key = input("Do you want to add more questions? (Y/N): ").upper()
    
    mycursor.close()
    mydb.close()
    home()
    


