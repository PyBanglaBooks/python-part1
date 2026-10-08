quiz = {
    "What is the capital of Bangladesh?": "Dhaka",
    "What is 5 + 5?": "10",
    "How many districts are in Bangladesh?": "64",
}

score = 0
for question, answer in quiz.items():
    user_answer = input(question + " ")
    if user_answer.strip().lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The answer is {answer}.")

print(f"Final score: {score}/{len(quiz)}")
