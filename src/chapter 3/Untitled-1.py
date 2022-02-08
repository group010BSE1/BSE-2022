def compute_pay(h,r):
    if h >40:
        xh= h -40
        pay=(1.5*r*xh)+(40*r)
        print(pay)
    else : 
        pay = h*r
        print(pay)
print(compute_pay(45,10))