"""модуль для роботи з файлами первинних даних
-зчитування та вивід на екран
"""

def get_dovidnyk():
    """повертає довідник товарних груп який отримує ззовні

    Returns:
        dovidnyk_list: довідник товарних груп
    """
    from_file = [
        "1000;  Тканини;             4",
        "2000;  Одяг та білизна;   7,5",
        "3000;  Взуття;            7,5",
        "4000;  Трикотаж;          7,5",
        "5000;  Галантерея;        9,5",
    ]
    # накопичувач товарів
    dovidnyk_list = []

    for line in from_file:
        line_list = line.split(';')
        dovidnyk_list.append(line_list)

    return dovidnyk_list

def show_dovidnyk(dovidnyk):    
    """виводить на екран список товарів заданого діапазону

    Args:
        dovidnyk ([list]): список товарів
    """



    tovar_code_from = input("З якого коду? ")
    tovar_code_to   = input("По який коду? ")

    for tovar in dovidnyk:

        if tovar_code_from < tovar[0] < tovar_code_to:
            print("код: {:5} найменування: {:25} скидка:{:10}".format(tovar[0], tovar[1], tovar[2]))


dovidnyk = get_dovidnyk()
show_dovidnyk(dovidnyk)
