# Q1 I am building some very high quality chairs and need exactly four nails for each chair.
# I have written a program to calculate how many nails I need to buy to build these charis

chairs = '15'
nails = 4

total_nails = int(chairs)* nails #turning the string chairs into an int

message = '{} nails'.format(total_nails)

print('You need to buy {}'.format(message))

# When I run the program it tells me that I need to buy 15151515 nails. There seems like a lot of nails
#Is my program calculating the total number correctly? What is the problem?
      
# Solution : The problem is that chairs is a string instead of an int so we need to turn the string '15' into an integer to perform multiplication instead of concatenation
      
