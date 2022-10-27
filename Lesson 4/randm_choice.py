import random

first_name = ['Victoria', 'GLoria', 'Ada', 'Grace']
last_name = ['Alred', 'Hopper', 'Lovelace', 'King']
random_first_name =random.choice(first_name)
random_last_name =random.choice(last_name)

print("Hello {} {}, nice to meet you!".format(random_first_name,random_last_name))
