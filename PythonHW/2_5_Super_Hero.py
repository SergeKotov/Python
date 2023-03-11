import requests

def get_super_hero_list():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url=url, timeout=5)
    return response.json()

if __name__ == '__main__':
    # define an objective
    heroes = ('Hulk', 'Captain America', 'Thanos')
    heroes_str = ', '.join(heroes)
    print(f'\nWho is the most intelligent super hero from: {heroes_str}?')
    
    # get response from API
    super_hero_list = get_super_hero_list()
    super_hero_short = filter(lambda hero: hero['name'] in heroes, super_hero_list)

    # find most intelligent
    max_IQ = 0
    hero_name = 'none'
    for hero in super_hero_short:
        iq = hero['powerstats']['intelligence']
        print(f"name: {hero['name']}, intelligence: {iq}")
        if iq > max_IQ:
            max_IQ = iq
            hero_name = hero['name']
    print(f'Most intelligent is {hero_name} with IQ {max_IQ}')
