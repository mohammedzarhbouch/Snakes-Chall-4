# lijst = []

# spelers = int(input("hoeveel spelers zijn er? \n"))
# for i in range (spelers):
#     print(input("wat is uw naam\n"))
#     lijst.append(spelers)
    
# print(lijst)


lijst1 = []
lijst2 = []
aantal_spelers = input("Hoeveel spelers zitten er in het team: ")
for i in range(int(aantal_spelers)):
    lijst1.append(input("Naam speler: "))
    lijst2.append(input("Aantal punten: "))

lijst2.sort(reverse = True)

print(f"de speler met deze score: {lijst2[0]} heeft gewonnen" )