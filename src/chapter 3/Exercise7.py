Location = input('Enter Job location: ')
Pay = input("enter pay : ")
try : 
    Pay = int(Pay)
    if Pay > 0 :
        raise ValueError
except ValueError :
    print("Input values.")
    exit()

if Pay > 4000000 and Location == "Mbarara" :
    print("Decision:", "Without dought, I'll take it.")
elif Pay >= 10000000 and Location == "Kampala" :
    print("Decision:", "Without dought, I'll take it.")
elif Pay >= 0 and Location == "Space" :
    print("Decision:", "Without dought, I'll take it.")
elif Pay < 10000000 and Location == "Kampala":
    print("Decision:", "No way!.")
elif Pay < 6000000 and Location == "Mbarara" :
    print("Decision:", "No thanks, I can find something better.")
elif Pay >= 6000000 and Location :
    print("Decision:", "Sure I can work with this.")
else:
    print("Decision:", "No thanks, I can find something better.")



