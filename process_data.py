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
                return dovidnyk_1[1]


     

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
        dohid_work['plan_1']        = dohid_work['plan'] * dohid_work['sale']
        dohid_work['vykonannya_1']  = dohid_work['vykonannya'] * dohid_work['sale']
        dohid_work['name_of_tovar'] = get_tovar_name(tovaroobih_1[0])

        dohid_list.append(dohid_work) 

    return dohid_list





dohids = create_dohid()

for item in dohids:
    print(item)



#print(get_tovaroobih())
#print(get_dovidnyk())