"""головний модуль задачі
- виводить на екран та в файл розрахункову таблицю
- виводить на екран первинні файли
"""
TABLE_STR = """============================================================================
Назва товару    | Рік   | План | Виконання | Знижка |   План1  |  Виконання1
============================================================================
"""
import os
import data_service, process_data
from process_data import create_dohid, format_dohid
from data_service import get_dovidnyk, get_tovaroobih, show_dovidnyk, show_tovaroobih, write_to_file


MAIN_MENU = """
~~~~~~~~~~~~~~~~~~~~~~~~ ОБРОВКА ВАЛОВОГО ДОХОДУ УНІВЕРМАГУ ~~~~~~~~~~~~~~~~~~~~~~~~ 

1 - вивід доходу на екран
2 - запис результата в файл
3 - вивід списку товарообігу
4 - вивід списку довідника
0 - завершення роботи
"""
while True:
    print(MAIN_MENU)
    com = input(">>  Введіть номер команди: ")

    if not com:
        os.system("clear")
    else:
        com = int(com)
        if com == 0:
            exit()
        
        elif com == 1:
            print(TABLE_STR)
            for item in create_dohid():
                print(format_dohid(item))
            enter = input("Натисніть <Enter>")
            os.system("clear")
        
        elif com == 3:
            show_tovaroobih(get_tovaroobih())
            enter = input("Натисніть <Enter>")
            os.system("clear")
        elif com == 4:
            show_dovidnyk(get_dovidnyk())
            enter = input("Натисніть <Enter>")
            os.system("clear")
        elif com == 2:
            question = input("Довідник чи товаробіг? ")
            if question == 'довідник':
                write_to_file(get_dovidnyk(), 'dovydnykWrite.txt', False)
            elif question == 'товарообіг':
                write_to_file(get_tovaroobih(), 'tovarWrite.txt', True)
            enter = input("Натисніть <Enter>")
            os.system("clear")

