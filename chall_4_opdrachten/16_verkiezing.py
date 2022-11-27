
v_lijst = []
lijst_lengte = 10000000

for i in range(lijst_lengte):
    item = input("voor wie stemt u: ")
    v_lijst.append(item)
    if item == "uitslag!":
        v_lijst.remove("uitslag!")
        break
    
def verkiezing(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = i
 
    return num

list = v_lijst
print(verkiezing(list))


