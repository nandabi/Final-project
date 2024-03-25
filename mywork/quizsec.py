import mysql.connector
import random

def quiz():
    print("Welcome to Quiz portal")
    print("***********************")

    # Connect to database
    mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="yourdatabase"
    )
    mycursor = mydb.cursor()

    # Fetch questions from the database
    mycursor.execute("SELECT * FROM question")
    questions = mycursor.fetchall()

    name = input("Enter your name: ")
    total_questions = len(questions)
    to_attempt = int(input(f"Enter the number of questions to attempt (max {total_questions}): "))

    # Randomly select question IDs
    question_ids = random.sample(range(1, total_questions + 1), min(to_attempt, total_questions))

    print("Quiz has started")
    score = 0
    for i, question_id in enumerate(question_ids, start=1):
        question = [q for q in questions if q[0] == question_id][0]
        print("--------------------------------------------------------------------------------------------")
        print(f"Q. {i}: {question[1]}\nA. {question[2]}\t\tB. {question[3]}\nC. {question[4]}\t\tD. {question[5]}")
        print("--------------------------------------------------------------------------------------------")
        
        # Get user's answer
        while True:
            choice = input("Answer (A, B, C, D): ").upper()
            if choice in ['A', 'B', 'C', 'D']:
                break
            else:
                print("Kindly select A, B, C, D as option only")
        
        # Check answer and update score
        if choice == question[6]:
            print("Correct")
            score += 1
        else:
            print(f"Incorrect. Correct answer is: {question[6]}")

    print(f"Quiz has ended!! Your final score is: {score}")

    # Insert user's score into the database
    mycursor.execute("SELECT * FROM users")
    user_id = mycursor.rowcount + 1
    mycursor.execute("INSERT INTO users VALUES (%s, %s, %s)", (user_id, name, score))
    mydb.commit()

    input("Press any key to continue: ")

