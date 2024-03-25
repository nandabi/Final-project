import random
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import Base, Question

# Create SQLite database engine
engine = create_engine('sqlite:///kenya_quiz.db')

# Create tables if they do not exist
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Insert questions if table is empty
if not session.query(Question).all():
    questions = [
        Question(question="What is the capital city of Kenya?", option_a="A. Nairobi", option_b="B. Mombasa", option_c="C. Kisumu", answer="A"),
        Question(question="Which mountain is the highest peak in Kenya?", option_a="A. Mount Kilimanjaro", option_b="B. Mount Elgon", option_c="C. Mount Kenya", answer="C"),
        Question(question="What is the name of the longest river in Kenya?", option_a="A. Tana River", option_b="B. Athi River", option_c="C. Ewaso Ng'iro River", answer="A"),
        Question(question="Which lake in Kenya is known for its flamingos?", option_a="A. Lake Victoria", option_b="B. Lake Naivasha", option_c="C. Lake Nakuru", answer="C"),
        Question(question="What is the name of the largest national park in Kenya?", option_a="A. Maasai Mara National Reserve", option_b="B. Tsavo National Park", option_c="C. Amboseli National Park", answer="B")
    ]
    session.add_all(questions)
    session.commit()

# Function to retrieve random question
def get_random_question():
    return session.query(Question).order_by(func.random()).first()

# Function to play the quiz game
def play_quiz():
    points = 0
    for _ in range(5):
        question = get_random_question()
        if question:
            print("\nQuestion:", question.question)
            print(question.option_a)
            print(question.option_b)
            print(question.option_c)
            user_answer = input("Your answer (A/B/C): ").strip().upper()
            if user_answer == question.answer:
                print("Correct!")
                points += 1
            else:
                print("Incorrect! The correct answer is:", question.answer)
        else:
            print("Error: No questions found in the database.")
            break

    print("\nQuiz completed!")
    print("Total points:", points)

# Main function
def main():
    print("Welcome to the Kenya Geography Quiz!")
    print("You will be asked 5 questions about Kenya's geographical facts.")
    print("Enter your answers as A, B, or C and see how many points you score.")

    play_quiz()

    print("\nThanks for playing!")

if __name__ == "__main__":
    main()
