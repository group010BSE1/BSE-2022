Hours = float(input("Enter your Hours: "))
Rate = float(input("Enter your rate: " ))
if Hours > 40 :
    new = (Hours - 40)
    payone = new * (1.5 * Rate)
    pay = payone + (40 * Rate)
else :
    pay = Hours * Rate
print(pay)
