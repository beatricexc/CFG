temperature = int(input("What is the temperature"))
                  
if temperature > 200:
    print("oven is too hot")
elif temperature < 150:
    print("The oven is too cold")
elif temperature == 180:
    print("The oven is at the perfect temperature")
else:
    print("Temperature is close enough")
