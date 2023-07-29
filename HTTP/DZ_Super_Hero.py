from operator import itemgetter

import requests


def comparison(list_name_hero):
    url = "https://akabab.github.io/superhero-api/api/all.json"
    data_hero = requests.get(url).json()
    list_hero = []
    for hero in data_hero:
        if hero["name"] in list_name_hero:
            list_hero.append([hero["name"], hero["powerstats"]["intelligence"]])
    max_intelligence = (max(list_hero, key=itemgetter(1)))
    return max_intelligence


if __name__ == '__main__':
    print(f'Самый умный это {(comparison(["Hulk", "Captain America", "Thanos"]))[0]}!!!')
