from tkinter import N


TOTAL= 0
Numbers = []
while True :
    Number = input('Enter number: ')
    try:
        if Number == 'Done':
            print(sum(Numbers))
            print(max(Numbers))
            print(min(Numbers))
            break
        Number = int(Number)
    except ValueError:
        print('Invalid input.')
        continue
   
    Number = int(Number)
    Numbers.append(Number)
