
num1 = int(input("geef mij het eerste nummer:\n"))
operatie = input("welke operatie (+, -, *, /, =,)?\n ")
if operatie == "=":
    print("Resultaat: ", num1)
    exit()
num2 = int(input("geef mij het tweede nummer:\n")) 
   

if operatie == "+":
    print("Resultaat: ", num1 + num2)
elif operatie == "-":
    print("Resultaat: ", num1 - num2)
elif operatie == "*":
    print("Resultaat: ", num1 * num2)
else: 
    print("Resultaat: ", num1 / num2)
    
    
    
