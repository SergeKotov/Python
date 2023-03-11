from pprint import pprint
import os

current = os.getcwd()
folder_name = 'PythonHW'

# Tasks: 1 and 2

file_name = '2_3_recipes.txt'
file_path = os.path.join(current, folder_name, file_name)
with open(file_path) as file:

    # 1 Make a dictionary

    cook_book = {}
    for line in file:
        dish = line.strip()
        ingredient_count = int(file.readline())
        ingredients = []
        for _ in range(ingredient_count):
            name, quantity, measure = file.readline().strip().split(' | ')
            ingredients.append(
                {'ingredient_name': name,
                 'quantity': int(quantity),
                 'measure': measure,
                }
            )
        cook_book[dish] = ingredients
        file.readline()

    print('\nКнига рецептов:')
    pprint(cook_book) # pretty print with a>z sort

    # 2 Get a shop list by dishes

    def get_shop_list_by_dishes(dish_names, person_count):
        ingredients = {}
        for name in dish_names:
            if name in cook_book:
                dish = cook_book[name]
                for ingredient in dish:
                    i_name = ingredient['ingredient_name']
                    value = ingredient['quantity'] * person_count
                    if i_name in ingredients:
                        ingredients[i_name]['quantity'] += value
                    else:                   
                        ingredients[i_name] = {'measure': ingredient['measure'], 'quantity': value}
            else:
                print(name + ' отсутствует в книге рецептов')
        return ingredients

    print('\nЛист покупок:')
    dish_names = ['Запеченный картофель', 'Омлет', 'Фахитос', 'Амброзия']
    person_count = 2
    print('Блюда: ' + ", ".join(dish_names))
    print(f'Количество персон: {person_count}')
    shop_list = get_shop_list_by_dishes(dish_names, person_count)
    pprint(shop_list)

# Task 3: merge files

file_names = ['2_3_1.txt', '2_3_2.txt', '2_3_3.txt']

# read content of the files as text lines
contents = []
for file_name in file_names:
    file_path = os.path.join(current, folder_name, file_name)
    with open(file_path) as file:
        contents.append(file.readlines())

# merge content and save the result to a new file
contents.sort(key=lambda x: len(x))
output_content = ''
for i in range(len(file_names)):
    output_content += file_names[i]
    output_content += f'\n{len(contents[i])}\n'
    output_content += "".join(contents[i]) + '\n'

file_path = os.path.join(current, folder_name, '2_3_output.txt')
with open(file_path, 'w') as file:
    file.write(output_content)

