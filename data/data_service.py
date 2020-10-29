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
            print("код: {:5} найменування: {:25} скидка:{:3}".format(tovar[0], tovar[1], tovar[2]))


dovidnyk = get_dovidnyk()
show_dovidnyk(dovidnyk)
    




def get_tovaroobih():
    """повертає товарообіг універмагу який отримує ззовні

    Returns:
        tovaroobih_list: товарообіг універмагу
    """
    from_file = [
        "1000;         4340;             4420;     2013",
        "2000;         6280;             6720;     2013",
        "3000;         5260;             5854;     2013",   
        "4000;         3720;             3682;     2013",
        "5000;         2410;             2694;     2013",
        "1000;         4600;             4640;     2014",
        "2000;         6800;             7400;     2014",
        "3000;         6000;             6250;     2014",
        "4000;         3800;             3850;     2014",
        "5000;         2700;             3000;     2014",
        "1000;         4700;             4625;     2015",
        "2000;         6700;             6630;     2015",
        "3000;         6700;             6500;     2015",
        "4000;         4300;             4500;     2015",
        "5000;         3500;             3590;     2015",
    ]

    # накопичувач унывермагу
    tovaroobih_list =[]

    for line in from_file:
        line_list = line.split(';')
        tovaroobih_list.append(line_list)
   
   
    return tovaroobih_list
 
def show_tovaroobih(tovaroobih):
    """виводить на екран товарообіг універмагу

    Args:
        tovaroobih ([list]): товарообіг універмагу
    """
    univermag_code_from = input("З якого коду? ")
    univermag_code_to   = input("По який коду? ")

    for univermag in tovaroobih:

        if univermag_code_from < univermag[0] < univermag_code_to:
           print(univermag)






tovaroobih = get_tovaroobih()
show_tovaroobih(tovaroobih)

