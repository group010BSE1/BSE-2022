



age = input("Enter Age : ")
try:
    age = int(age)
    if age < 0:
        raise ValueError
    if age >= 18:
        print("You can vote")
    else:
        print("Too young to vote")
except ValueError:
    print("Are you a time traveller")

