from ast import Raise


TOTAL= 0
x = 0
while True :
    Number = input('Enter number: ').capitalize()
    try:
        if Number == 'Done':
            print(TOTAL, x, TOTAL/x)
            break
        Number = int(Number)
    except ValueError:
        print('Invalid input.')
        continue
   
    Number = int(Number)
    TOTAL = TOTAL + Number
    x = x + 1
            

            

