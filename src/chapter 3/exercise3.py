marks = input("Enter Marks : ")
try:
    if float(marks) > 1 or float(marks) < 0:
        raise ValueError

except ValueError:
    print("Bad Score")
    exit()

m = float(marks)

if m >= 0.9:
    print("A")
elif m >= 0.8:
    print("B")
elif m >= 0.7:
    print("C")
elif m >= 0.6:
    print("D")
else:
    print("F")