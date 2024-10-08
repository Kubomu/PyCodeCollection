"""
Run a Formula One quiz with 5 questions.

The quiz will ask the user to answer each question by entering the number of the correct option.
The score will be displayed at the end of the quiz.

Example:
    >>> run_quiz()
    Welcome to the F1 Quiz!
    ... (quiz questions and answers)
    Quiz completed! Your score: 3/5

:param: None
:return: None
"""
def run_quiz():
    questions = [
    {"question": "Which Formula One driver has won the most World Championships?", "options": ["Lewis Hamilton", "Michael Schumacher", "Sebastian Vettel"], "answer": "Michael Schumacher"},
    {"question": "What is the name of the famous Formula One track in Monaco?", "options": ["Monza", "Silverstone", "Circuit de Monaco"], "answer": "Circuit de Monaco"},
    {"question": "Which Formula One team has won the most Constructors' Championships?", "options": ["Ferrari", "Mercedes", "Red Bull Racing"], "answer": "Ferrari"},
    {"question": "Who is the current CEO of the Formula One Group?", "options": ["Chase Carey", "Liberty Media", "Bernie Ecclestone"], "answer": "Chase Carey"},
    {"question": "What is the name of the Formula One tyre supplier?", "options": ["Pirelli", "Michelin", "Goodyear"], "answer": "Pirelli"}
]

    score = 0

    print("Welcome to the F1 Quiz!")

    for question in questions:
        print("\n" + question["question"])
        for i, option in enumerate(question["options"], 1):
            print(f"{i}. {option}")

        user_answer = input("Your answer (enter the number): ")

        if user_answer.isdigit() and 1 <= int(user_answer) <= len(question["options"]):
            selected_option = question["options"][int(user_answer) - 1]
            if selected_option == question["answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {question['answer']}")
        else:
            print("Invalid input. Skipping this question.")

    print(f"\nQuiz completed! Your score: {score}/{len(questions)}")

# Run the quiz
run_quiz()