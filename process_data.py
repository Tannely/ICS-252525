"""формування валового доходу універмагу
"""

from data_service import get_dovidnyk, get_tovaroobih

# структура запису для вхідних даних
dohid = {
    'name_of_tovar' : '',    # найменування товарної групи
    'year' : '',             # рік
    'plan' : 0.0,            # план товарообігу
    'vykonannya' : 0.0,      # очікуване виконання товаробігу
    'sale' : 0.0,            # торгова скидка
    'plan_1' : 0.0,          # план валового доходу 
    'vykonannya_1' : 0.0     # очікуване виконання валового доходу
}

def create_dohid():
    """формування списку доходу

    Returns:
        dohid_list: список доходу
    """

    def get_tovar_name(tovar_code):
        """знаходить назву товару по коду

        Args:
            tovar_code ([type]): код товару

        Returns:
            [type]: назву товару
        """
        for dovidnyk_1 in dovidnyk:
            if tovar_code == dovidnyk_1[0]:
                return (dovidnyk_1[1], dovidnyk_1[2])


     

    # накопичувач вхідних даних
    dohid_list = []

    tovaroobih = get_tovaroobih()
    dovidnyk = get_dovidnyk()


    for tovaroobih_1 in tovaroobih:

        #робоча змінна
        dohid_work = dohid.copy() 

        dohid_work['year']          = tovaroobih_1[3]
        dohid_work['plan']          = tovaroobih_1[1]
        dohid_work['vykonannya']    = tovaroobih_1[2]
        dohid_work['name_of_tovar'] = get_tovar_name(tovaroobih_1[0])[0]
        dohid_work['sale']          = get_tovar_name(tovaroobih_1[0])[1]
        dohid_work['plan_1']        = dohid_work['plan'] * dohid_work['sale']
        dohid_work['vykonannya_1']  = dohid_work['vykonannya'] * dohid_work['sale']
        dohid_list.append(dohid_work) 

    return dohid_list






def format_dohid(dohid):
    return f'{dohid.get("name_of_tovar"):15} | {dohid.get("year"):5} | {dohid.get("plan"):4} |   {dohid.get("vykonannya")}    |   {dohid.get("sale"):3}  | {dohid.get("plan_1"):8} | {dohid.get("vykonannya_1"):8}'


#print(get_tovaroobih())
#print(get_dovidnyk())