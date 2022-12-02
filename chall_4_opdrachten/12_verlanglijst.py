
inputs = []
while True:
    inp = input("wat wil jij voor sinterklaas? type KLAAR als je klaar bent:\n")
    if inp == "KLAAR":
        break
    inputs.append(inp)
    
inputs.sort()
print(inputs)