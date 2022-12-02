import random

def open_box():
    if random.randint(1,100) <= 5:
        return ("legendary item")
    elif random.randint(1,100) <= 15:
        return("epic item")
    elif random.randint(1,100) <= 30:
        return("rare item")
    elif random.randint(1,100) <= 50:
        return("uncommon item")
    else:
        return("common item")
    
    
for i in range(1):
    print(open_box()) 
