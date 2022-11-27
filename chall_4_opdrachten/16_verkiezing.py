
v_lijst = []
lijst_lengte = 10000000

for item in range(lijst_lengte):
    item = input("voor wie stemt u: ").lower()
    v_lijst.append(item)
    if item == "UITSLAG!":
        v_lijst.remove("UITSLAG!")
        break
    
def verkiezing(List):
    counter = 0
    names = List[0]
     
    for item in List:
        curr_frequency = List.count(item)
        if(curr_frequency > counter):
            counter = curr_frequency
            names = item
        
 
    return names

list = v_lijst
print(verkiezing(list))



