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

print(get_tovaroobih())
print(get_dovidnyk())