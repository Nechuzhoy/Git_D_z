

mentors = [
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

# Объединить списки преподавателей по всем курсам
all_list = []
def create_all_list(mentors):

    [all_list.extend(x) for x in mentors]
    return  all_list


#Отделить имя от фамилии
def create_all_names_list(all_list):
    all_names_list = [x.split(" ")[0].strip() for x in all_list]
    return all_names_list


# Убрать дубли при помощи множеств
def list_in_set(all_list):
    return set(create_all_names_list(all_list))



if __name__ == '__main__':
    create_all_list(mentors)
    # Подсчитываем встречаемость каждого имени
    popular = [[create_all_names_list(all_list).count(x), x] for x in list_in_set(all_list)]
    # Сортируем по убыванию встречаемости
    popular.sort(key=lambda x: x[0], reverse=True)  # сортировка ключ 0 элемент списка
    # Выводим топ-3 имён
    top_3 = [f"{str(x[1])}: {str(x[0])} раз(а)" for x in popular[:3]]
    print(", ".join(top_3))
