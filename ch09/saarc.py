saarc = ["Bangladesh", "Afghanistan", "Bhutan", "Nepal", "India", "Pakistan", "Sri Lanka"]
country = input("Enter the name of the country: ")

if country in saarc:
    print(f"{country} is a member of SAARC")
else:
    print(f"{country} is not a member of SAARC")
