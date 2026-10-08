# অধ্যায় ৩, অনুশীলনী ৩

marks = int(input("Please enter your marks: "))

if marks > 100 or marks < 0:
    print("Invalid marks")
else:
    if marks >= 80:
        grade = "A+"
    elif marks >= 70:
        grade = "A"
    elif marks >= 60:
        grade = "A-"
    elif marks >= 50:
        grade = "B"
    elif marks >= 40:
        grade = "C"
    elif marks >= 33:
        grade = "D"
    else:
        grade = "F"
    print(f"Your grade is {grade}")
