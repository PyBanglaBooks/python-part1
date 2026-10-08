# অধ্যায় ১৪, অনুশীলনী ৩

quiz = {}
with open("quiz.txt", "r", encoding="utf-8") as f:
    for line in f:
        question, answer = line.strip().split(",")
        quiz[question] = answer

score = 0
for question, answer in quiz.items():
    user_answer = input(question + " ")
    if user_answer.strip().lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The answer is {answer}.")

print(f"Final score: {score}/{len(quiz)}")
