from pprint import pprint


def in_join(file_txt):
    with open(file_txt, encoding='utf-8') as file:
        dish = {}
        for line in file:
            dish_name = line.strip()
            ingrs_count = file.readline()
            ingrs = []
            for i in range(int(ingrs_count)):
                ing = file.readline()
                ingredient_name, quantity, measure = ing.strip().split(
                    ' | ')
                ingredients = {
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure,

                }
                ingrs.append(ingredients)
            file.readline()
            dish[dish_name] = ingrs
    return dish


def get_shop_list_by_dishes(dishes, person_count):
    dish = in_join("cool_book.txt")
    dic = {}
    for ing_dic in dishes:
        ingr = dish.get(ing_dic)
        for dish_num in ingr:
            if dish_num['ingredient_name'] in dic:
                dic[(dish_num.get('ingredient_name')) + " для " + ing_dic] = {'measure': dish_num.get('measure'),
                                                                              'quantity': (int(dish_num.get(
                                                                                  'quantity')) * person_count)}
            else:
                dic[dish_num.get('ingredient_name')] = {'measure': dish_num.get('measure'),
                                                        'quantity': (int(dish_num.get('quantity')) * person_count)}
    return dic


a = get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
pprint(a)
