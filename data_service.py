"""модуль для роботи з файлами первинних даних
-зчитування та вивід на екран
"""


def get_dovidnyk():
    """повертає довідник товарних груп який отримує  з файлу 'dovidnyk.txt'

    Returns:
        dovidnyk_list: довідник товарних груп
    """

    with open("./data/dovidnyk.txt") as dovidnyk_file:
        from_file = dovidnyk_file.readlines()

    # накопичувач клієнтів
    dovidnyk_list = []

    for line in from_file:
        #відрізати '\n' в кінці рядка
        line = line[:-1]
        line_list = line.split(';')
        line_list[2] = float(line_list[2])
        dovidnyk_list.append(line_list)

    return dovidnyk_list


def show_dovidnyk(dovidnyk):
    """виводить на екран список товарів заданого діапазону

    Args:
        dovidnyk ([list]): список товарів
    """

    tovar_code_from = input("З якого коду? ")    
    tovar_code_to   = input("По який код? ")

    

    for tovar in dovidnyk:
        if tovar_code_from <= tovar[0] <= tovar_code_to:
            print("Код: {:5} Найменування: {:21} Знижка: {:5}".format(tovar[0], tovar[1], tovar[2]))
            



#dovidnyk = get_dovidnyk()
#show_dovidnyk(dovidnyk)



def get_tovaroobih():
    """повертає товарообіг універмагу який отримує з файлу 'tovaroobih.txt'

    Returns:
        tovaroobih_list: товарообіг універмагу
    """

    with open("./data/tovaroobih.txt") as tovaroobih_file:
        from_file = tovaroobih_file.readlines()

    #накопичувач універмагу
    tovaroobih_list = []

    for line in from_file:
        #відрізати '\n' в кінці рядка
        line = line[:-1]
        line_list = line.split(';')
        line_list[1] = int(line_list[1])
        line_list[2] = int(line_list[2])
        tovaroobih_list.append(line_list)

    return tovaroobih_list

def show_tovaroobih(tovaroobih):
    """виводить на екран товарообіг універмагу

    Args:
        tovaroobih ([list]): товарообіг універмагу
    """

    univermag_code_from = input("З якого коду? ")
    univermag_code_to   = input("По який код? ")

    

    for univermag in tovaroobih:
        if univermag_code_from <= univermag[0] <= univermag_code_to:
            print("Код: {:6} План: {:6} Виконання: {:6} Рік: {:6}".format(univermag[0], univermag[1], univermag[2], univermag[3]))
           

#tovaroobih = get_tovaroobih()
#show_tovaroobih(tovaroobih)    