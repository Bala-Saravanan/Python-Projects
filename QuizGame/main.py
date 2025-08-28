print("🎮 Welcome to the Python Quiz Game!")
print("Answer the following questions by typing A, B, C, or D.\n")

# Questions, options, and answers
questions = [
    {
        "question": "Who is the creator of the Python programming language?",
        "options": [
            "A. James Gosling",
            "B. Dennis Ritchie",
            "C. Guido van Rossum",
            "D. Bjarne Stroustrup"
        ],
        "answer": "C"
    },
    {
        "question": "Python is a dynamically typed language. What does this mean?",
        "options": [
            "A. Variables can change type during execution",
            "B. Types of variables are checked only at runtime",
            "C. You must declare the type of variable explicitly",
            "D. Python does not support static typing at all"
        ],
        "answer": "B"
    },
    {
        "question": "Python is called an interpreted language. What does this mean?",
        "options": [
            "A. Python code is converted directly into machine code",
            "B. Python code is executed line by line at runtime",
            "C. Python code must always be compiled before running",
            "D. Python cannot run on different operating systems"
        ],
        "answer": "B"
    },
    {
        "question": "What symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. /* */"],
        "answer": "C"
    },
    {
        "question": "Which of the following is a mutable data type in Python?",
        "options": ["A. Tuple", "B. List", "C. String", "D. Integer"],
        "answer": "B"
    },
    {
        "question": "How many times the loop will run?\n\ni = 0\nwhile i > 0:\n    print(i)\n    i += 1\n",
        "options": [
            "A. 0 times",
            "B. 1 time",
            "C. Infinite times",
            "D. Error"
        ],
        "answer": "A"
    },
    {
        "question": "What will this code print?\n\nfor i in range(10, 0, -2):\n     print(i)\n",
        "options": [
            "A. 0, 2, 4, 6, 8",
            "B. 2, 4, 6, 8, 10",
            "C. 10, 8, 6, 4, 2",
            "D. -10, -8, -6, -4, -2"
        ],
        "answer": "C"
    },
    {
        "question": "What is the file extension for Python files?",
        "options": ["A. .java", "B. .py", "C. .exe", "D. .txt"],
        "answer": "B"
    },
    {
        "question": "Which operator is used for exponentiation in Python?",
        "options": ["A. ^", "B. **", "C. //", "D. %"],
        "answer": "B"
    },
    {
        "question": "What will the following code print?\n\nfor i in range(2):\n    for j in range(2):\n        print(i, j)\n",
        "options": [
            "A. 0 0 0 1 1 0 1 1",
            "B. 0 0 1 1",
            "C. 0 1 0 1",
            "D. 0 0 1 0"
        ],
        "answer": "A"
    }
]

score = 0

# Loop through each question
for i, q in enumerate(questions, 1):
    print(f"\nQ{i}: {q['question']}")
    for option in q['options']:
        print(option)
    
    answer = input("Your answer: ").upper()

    if answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was {q['answer']}.")

print("\n🎉 Quiz Over!")
print(f"Your final score: {score}/{len(questions)}")
