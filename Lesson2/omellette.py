
#Question 3 

#I have a lot of boxes of eggs in my fridge and I want to calculate how many omelettes I can make. Write a program to calculate this. 
#Assume that a box of eggs contains six eggs and I need four eggs for each omelette, but I should be able to easily change these values if I want.
#The output should say something like "You can make 9 omelettes with 6 boxes of eggs". 

num_boxes = int(input("How many boxes of eggs in the fridge? "))
egg_box = int(input("how many eggs in the box?"))
omelette = int((num_boxes*egg_box) / 4)
print(f'You can make {omelette} omelettes with {num_boxes} boxes of eggs.'.format(omelette,num_boxes))
