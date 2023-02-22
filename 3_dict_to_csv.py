"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    import csv 

    user_list = [
           {'name': 'Kara', 'age': '28', 'job': 'developer'},
           {'name': 'Steve', 'age': '34', 'job': 'manager'},
           {'name': 'John', 'age': '41', 'job': 'CEO'},
           {'name': 'Lucy', 'age': '23', 'job': 'tester'}
    ]

    with open('user_list.csv', 'w', encoding='utf-8', newline='') as list:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(list, fields, delimiter=';')
        writer.writeheader()
        for user in user_list:
            writer.writerow(user)

if __name__ == "__main__":
    main()
