import random as r
import requests

def random_pokemon():
    pokemon_number = r.randint(1,151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return{
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'order': pokemon['order']
    }

def run():
    my_pokemon = random_pokemon()

    print('You were given {}'.format(my_pokemon['name']))
    stat_choice = input('Which stat do you want to use? (id, height, weight, order)')

    opponent_pokemon = random_pokemon()
    print('The opponent chose {} '.format(opponent_pokemon['name']))

    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]

    if my_stat > opponent_stat :
        print("You win!")
    elif my_stat < opponent_stat:
        print("You lose!")
    else:
        print("Draw!")

for i in range(5):
    random_pokemon()
    run()
