from pprint import pprint

def buid_dictionary(list):  # Метод для постройки словаря
    rate = ['ingredient_name', 'quantity', 'measure']
    lst1 = list.split('|')
    myDict = {rate[i]: lst1[i] for i in range(0, len(rate), 1)}
    return myDict

def get_book_cook():
    book_cook = {}
    with open('Cook_book.txt', 'r', encoding='utf-8') as file:  # Читаем файл
        lines = [line.rstrip() for line in file]
        eggs = lines[0:5]
        berd = lines[6:12]
        potato = lines[13:18]
        eggs_menu = eggs[0:1]
        berd_menu = berd[0:1]
        potato_menu = potato[0:1]
    # Формируем списки
    menu = eggs_menu + berd_menu + potato_menu
    ingridient_eggs = eggs[2:5]
    ingridient_berd = berd[2:6]
    ingridient_potato = potato[2:5]
    ingridient = ingridient_eggs + ingridient_berd + ingridient_potato

    eggs_book = []
    for lst in ingridient_eggs:
        eggs_book.append(buid_dictionary(lst))
    key, value = eggs_menu[0], eggs_book
    book_cook[key] = value

    berd_book = []
    for lst in ingridient_berd:
        berd_book.append(buid_dictionary(lst))
    key, value = berd_menu[0], berd_book
    book_cook[key] = value

    potato_book = []
    for lst in ingridient_potato:
        potato_book.append(buid_dictionary(lst))
    key, value = potato_menu[0], potato_book
    book_cook[key] = value

    return book_cook

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_book_cook()

    dict_result = {}
    for dish in dishes:
        for k in cook_book:

            if dish == k:
                for n in cook_book[k]:
                    dict_value = {}
                    key, value = 'measure', n['measure']
                    dict_value[key] = value

                    key, value = 'quantity', int(n['quantity']) * person_count
                    dict_value[key] = value

                    key, value = n['ingredient_name'], dict_value
                    dict_result[key] = value

    pprint(dict_result)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
