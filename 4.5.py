b = input("enter number: ")

""" створюємо функцію, що буде приймати строку в якості параметра і перетворювати її
в число з плаваючою точкою, додаємо виключення, що вводити можна тільки числа
"""

def convert_func(parametr):
    try:
        return float(parametr)
    except ValueError:
        print("тільки числа")
c = convert_func(b)
print(c)
