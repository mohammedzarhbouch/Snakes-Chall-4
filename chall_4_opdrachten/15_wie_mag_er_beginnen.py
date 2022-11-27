import random

lijst1 = []

aantal_spelers = input("Hoeveel spelers zitten er in het team: ")
for i in range(int(aantal_spelers)):
    lijst1.append(input("Naam speler: "))
    
print(random.choice(lijst1))