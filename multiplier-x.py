tafels = int(input("welke tafel wil je zien? "))

def calculator(tafels):
    
    for e in range(1,11):
        antwoord = e*tafels
        print(e, "x" ,tafels, "=",str(antwoord))
    
calculator(tafels)
