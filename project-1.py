import random

# -----------------------------------------
# PYTHON QUIZ APPLICATION
# -----------------------------------------

questions = {
    "Python": [
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["func", "define", "def", "function"],
            "answer": 3
        },
        {
            "question": "Which data type stores key-value pairs?",
            "options": ["List", "Tuple", "Dictionary", "Set"],
            "answer": 3
        },
        {
            "question": "Which symbol is used for a single-line comment in Python?",
            "options": ["//", "#", "/*", "--"],
            "answer": 2
        },
        {
            "question": "Which method is used to add an item to a list?",
            "options": ["add()", "insert()", "append()", "push()"],
            "answer": 3
        },
        {
            "question": "What is the output of len([10, 20, 30])?",
            "options": ["2", "3", "4", "30"],
            "answer": 2
        }
    ],

    "Computer Science": [
        {
            "question": "What does CPU stand for?",
            "options": [
                "Central Processing Unit",
                "Computer Processing Unit",
                "Central Program Unit",
                "Control Processing Unit"
            ],
            "answer": 1
        },
        {
            "question": "Which number system uses only 0 and 1?",
            "options": ["Decimal", "Binary", "Octal", "Hexadecimal"],
            "answer": 2
        },
        {
            "question": "What does RAM stand for?",
            "options": [
                "Read Access Memory",
                "Random Access Memory",
                "Rapid Access Module",
                "Run Access Memory"
            ],
            "answer": 2
        },
        {
            "question": "Which data structure follows FIFO?",
            "options": ["Stack", "Queue", "Tree", "Graph"],
            "answer": 2
        },
        {
            "question": "Which one is an operating system?",
            "options": ["Python", "Linux", "HTML", "SQL"],
            "answer": 2
        }
    ],

    "General Knowledge": [
        {
            "question": "What is the capital of India?",
            "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
            "answer": 2
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Venus", "Mars", "Jupiter"],
            "answer": 3
        },
        {
            "question": "How many continents are there?",
            "options": ["5", "6", "7", "8"],
            "answer": 3
        },
        {
            "question": "Which is the largest ocean on Earth?",
            "options": [
                "Indian Ocean",
                "Atlantic Ocean",
                "Pacific Ocean",
                "Arctic Ocean"
            ],
            "answer": 3
        },
        {
            "question": "Which gas is most abundant in Earth's atmosphere?",
            "options": [
                "Oxygen",
                "Nitrogen",
                "Carbon Dioxide",
                "Hydrogen"
            ],
            "answer": 2
        }
    ]
}


# -----------------------------------------
# FUNCTION TO DISPLAY HEADER
# -----------------------------------------

def display_header():
    print("\n" + "=" * 55)
    print("             PYTHON QUIZ APPLICATION")
    print("=" * 55)


# -----------------------------------------
# FUNCTION TO CHOOSE CATEGORY
# -----------------------------------------

def choose_category():
    print("\nChoose a Quiz Category:")
    print("1. Python")
    print("2. Computer Science")
    print("3. General Knowledge")
    print("4. Mixed Quiz")

    while True:
        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            return "Python"
        elif choice == "2":
            return "Computer Science"
        elif choice == "3":
            return "General Knowledge"
        elif choice == "4":
            return "Mixed"
        else:
            print("Invalid choice! Please enter 1, 2, 3 or 4.")


# -----------------------------------------
# FUNCTION TO GET QUESTIONS
# -----------------------------------------

def get_questions(category):
    if category == "Mixed":
        all_questions = []

        for category_questions in questions.values():
            all_questions.extend(category_questions)

        random.shuffle(all_questions)
        return all_questions

    selected_questions = questions[category].copy()
    random.shuffle(selected_questions)

    return selected_questions


# -----------------------------------------
# FUNCTION TO PLAY QUIZ
# -----------------------------------------

def play_quiz():
    display_header()

    name = input("\nEnter your name: ").strip()

    if name == "":
        name = "Player"

    category = choose_category()
    quiz_questions = get_questions(category)

    # Ask how many questions
    maximum = len(quiz_questions)

    while True:
        try:
            number = int(
                input(
                    f"\nHow many questions do you want to attempt "
                    f"(1-{maximum})? "
                )
            )

            if 1 <= number <= maximum:
                break
            else:
                print(f"Please enter a number between 1 and {maximum}.")

        except ValueError:
            print("Please enter a valid number.")

    quiz_questions = quiz_questions[:number]

    score = 0

    print("\n" + "-" * 55)
    print(f"Player   : {name}")
    print(f"Category : {category}")
    print(f"Questions: {number}")
    print("-" * 55)

    # -----------------------------------------
    # ASK QUESTIONS
    # -----------------------------------------

    for question_number, question in enumerate(
        quiz_questions, start=1
    ):

        print(
            f"\nQuestion {question_number}/{number}"
        )

        print(question["question"])

        print()

        for option_number, option in enumerate(
            question["options"], start=1
        ):
            print(f"{option_number}. {option}")

        # Get answer
        while True:
            try:
                answer = int(
                    input("\nEnter your answer (1-4): ")
                )

                if 1 <= answer <= 4:
                    break
                else:
                    print("Please enter a number from 1 to 4.")

            except ValueError:
                print("Please enter a valid number.")

        # Check answer
        if answer == question["answer"]:
            print("Correct! ✓")
            score += 1
        else:
            correct_answer = question["answer"]

            print("Wrong! ✗")
            print(
                "Correct answer:",
                question["options"][correct_answer - 1]
            )

    # -----------------------------------------
    # CALCULATE RESULT
    # -----------------------------------------

    percentage = (score / number) * 100

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    # -----------------------------------------
    # DISPLAY RESULT
    # -----------------------------------------

    print("\n")
    print("=" * 55)
    print("                 QUIZ RESULT")
    print("=" * 55)

    print(f"Name       : {name}")
    print(f"Category   : {category}")
    print(f"Score      : {score}/{number}")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Grade      : {grade}")

    print("=" * 55)

    if percentage >= 80:
        print("Excellent performance! 🎉")
    elif percentage >= 60:
        print("Good job! Keep improving. 👍")
    elif percentage >= 40:
        print("Nice attempt! Practice more. 📚")
    else:
        print("Keep practicing and try again! 💪")

    print("=" * 55)


# -----------------------------------------
# MAIN PROGRAM
# -----------------------------------------

def main():

    while True:

        display_header()

        print("\n1. Start Quiz")
        print("2. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            play_quiz()

            # Ask if user wants another quiz
            while True:
                again = input(
                    "\nDo you want to play another quiz? (y/n): "
                ).lower()

                if again == "y":
                    break

                elif again == "n":
                    print("\nThank you for using Quiz Application!")
                    return

                else:
                    print("Please enter y or n.")

        elif choice == "2":
            print("\nThank you for using Python Quiz Application!")
            print("Goodbye! 👋")
            break

        else:
            print("\nInvalid choice! Please select 1 or 2.")


# -----------------------------------------
# PROGRAM START
# -----------------------------------------

if __name__ == "__main__":
    main()
