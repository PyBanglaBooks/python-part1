# অধ্যায় ১৪, অনুশীলনী ৫

names = ["Rahim", "Karim", "Tania", "Sumon", "Rafi", "Aarav"]
marks = [55, 90, 45, 80, 32, 67]

passed = 0
failed = 0
for name, mark in zip(names, marks):
    if mark >= 33:
        print(f"{name}: Pass")
        passed += 1
    else:
        print(f"{name}: Fail")
        failed += 1

print(f"Passed: {passed}, Failed: {failed}")
