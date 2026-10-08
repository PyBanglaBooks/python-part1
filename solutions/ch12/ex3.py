# অধ্যায় ১২, অনুশীলনী ৩

districts = {"Barishal": 6, "Chattogram": 11, "Dhaka": 13,
             "Khulna": 10, "Mymensingh": 4, "Rajshahi": 8,
             "Rangpur": 8, "Sylhet": 4}

best = ""
best_count = 0
for division in districts:
    if districts[division] > best_count:
        best = division
        best_count = districts[division]

print(f"{best} has the most districts: {best_count}")
