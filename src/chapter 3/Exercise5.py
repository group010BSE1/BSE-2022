Attendants = input("Enter the number of people attending : ")
try :
    Attendants= int(Attendants)
    if Attendants < 0  :
        raise ValueError 
    if Attendants <=50 :
        print("Cost is $4000")
    elif Attendants <=100 :
        print("cost is $10000")
    elif Attendants <=200 :
        print("cost is $15000")
    else:
        print("cost is $20000")
except ValueError:
    print("Enter valid input")
     


