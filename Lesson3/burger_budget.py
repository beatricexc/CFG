
al_price = float(input('How much did the meal cost? '))
discount_choice = input('Do you have a discount? y/n ')
discount_applicable = discount_choice == 'y'
meal_price_ok =meal_price >20
if meal_price_ok and discount_applicable:
    meal_price = meal_price * 0.9
    print("Discount applied")
    print('Total cost is {}'.format(meal_price))
else:
    print("No discount")

