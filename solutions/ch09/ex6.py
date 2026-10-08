# অধ্যায় ৯, অনুশীলনী ৬

def positives(numbers):
    result = []
    for n in numbers:
        if n > 0:
            result.append(n)
    return result

numbers = [3, -1, 0, 7, -5, 2]
print(positives(numbers))
print(numbers)
