v_lijst = []

lijst_lengte = 10000000

for i in range(lijst_lengte):
    item = input("wat wil jij voor sinterklaas: ")
    v_lijst.append(item)
    if item == "klaar":
        v_lijst.remove("klaar")
        break
    
    
print(v_lijst)
