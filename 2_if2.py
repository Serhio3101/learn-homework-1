"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
     
    str1 = input("Введите первую строку: ")
    str2 = input("Введите вторую строку: ")
    
    if type(str1) != str and type(str2)!= str :
        return 0
    if str1 == str2 :
        return 1
    if len(str1) > len(str2) :
        return 2
    if str1 != str2 and str2 == "learn" :
        return 3
    else :
        return "Нет подходящего ответа"
    
            
if __name__ == "__main__":
    while True:
        print(f'Результат: {main()}')

    