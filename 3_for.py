"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
phone_sold = [
  {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
  {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
  {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]}
]

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    allsum = 0
    mean = 0
    def allsum_one_phone(allitems_sold):
        sum_one_phone_sold = 0
        for sold in allitems_sold:
            sum_one_phone_sold = sum_one_phone_sold + sold
        return sum_one_phone_sold
    
    for product in phone_sold:
        items_sold = allsum_one_phone(product["items_sold"])    
        print(f'Среднее количество продаж {product["product"]}: {items_sold/len(product["items_sold"])}')
        print(f'Cуммарное количество продаж {product["product"]}: {items_sold}')
        allsum = allsum + items_sold
        mean = mean + items_sold/len(product["items_sold"])

    mean = mean / len(phone_sold)
    
    print(f'Cуммарное количество продаж всех товаров: {allsum}')
    print(f'Cреднее количество продаж всех товаров: {mean}')   
    
       

if __name__ == "__main__":
    main()
