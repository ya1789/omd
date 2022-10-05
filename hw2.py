import csv
import string
path = '/home/kseniya/Downloads/Corp_Summary.csv'


def get_unique(seq: object) -> list:
    """
    Возвращает уникальные элементы
    :param seq: object
    """

    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]


def reading_data(path: string) -> list:
    """
    Записывает данные в лист
    :param path: string
    """

    with open(path, 'r') as file:
        my_reader = csv.reader(file, delimiter=';')
        data = []
        for row in my_reader:
            data.append(row)
        data.pop(0)
    return data


def get_hierarchy(data: list):
    """
    Выводит иерархию команд по департаментам
    :param data: 2d array
    """

    result = {}
    list_of_depart = []
    for row in data:
        list_of_depart.append([row[1], row[2]])
        for element in list_of_depart:
            if element[0] in result:
                result[element[0]] = result.get(element[0], []) + [element[1]]
                result[element[0]] = get_unique(result[element[0]])
            else:
                result[element[0]] = element

    for key, value in result.items():
        print('Департамент:', key, end='\n')
        print('Команды:', ', '.join(value[1:]), end='\n\n')


def get_stats(data: list) -> list:
    """
    Создает список со статистикой
    Возвращает список с данными
    :param data: 2d array
    """

    all_departments = []
    for item in data:
        all_departments.append(item[1])
    all_departments = set(all_departments)
    salary = []
    number = 0
    future_csv = []
    for dep in all_departments:
        for item in data:
            if item[1] == dep:
                salary.append(int(item[5]))
                number += 1
        s = [dep, number, min(salary), max(salary),
             round(sum(salary) / number, 2)]
        future_csv.append(s)
        salary = []
        number = 0
    return future_csv


def get_new_csv():
    """
    Построчно сохраняет статистику по департаментам в .csv
    """
    COLUMNS = ['Название', 'Численность', 'Мин ЗП', 'Макс ЗП', 'Avg ЗП']
    with open('Новый отчет.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(COLUMNS)
        write.writerows(get_stats(reading_data(path)))


def menu_for_choice(path: string):
    """
    Описывает пользователю функционал
    Выводит кнопки
    :param path: string
    """
    options = {'Вывести иерархию команд - введите цифру 1': 1,
               'Вывести отчет по департаментам - введите цифру 2': 2,
               'Сохранить отчет по департаментам  - введите цифру 3': 3,
               'Покинуть меню - введите цифру 4': 4}
    option = 0
    while option != '4':
        print('Выберите подходящее '
              'и введите цифру:\n{}\n{}\n{}\n{}'.format(*options))
        option = input()
        if option == '1':
            get_hierarchy(reading_data(path))
        elif option == '2':
            print('Сводный отчет')
            for row in get_stats(reading_data(path)):
                print(f'Департамент: {row[0]}, Количество сотрудников: {row[1]},',
                      f'Мин. зп: {row[2]}, Макс. зп: {row[3]},',
                      f'Avg. зп: {row[4]}')
                print()
        elif option == '3':
            get_new_csv()


menu_for_choice(path)