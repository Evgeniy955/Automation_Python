def addition(a, b):
    '''Операция сложения'''
    return a + b


def subtraction(a, b):
    '''Операция вычитания'''
    return a - b


def multiplication(a, b, r):
    '''Операция умножения с округлением'''
    if r == 0:
        return round(a * b)
    else:
        return round(a * b, r)


def division(a, b, r):
    '''Операция деления с округлением и обработка ошибки ZeroDivisionError'''
    try:
        res_1 = a / b
        if r == 0:
            return round(res_1)
        else:
            return round(res_1, r)
    except ZeroDivisionError:
        print("Нельзя делить на 0")


def calc():
    '''Функция обработки результатов'''
    res = input("Введите данные (example 2+2): ")
    if "+" in res:
        a = float(res.split("+")[0])
        b = float(res.split("+")[1])
        print("Ваш результат: ", addition(a, b))
    elif "-" in res:
        a = float(res.split("-")[0])
        b = float(res.split("-")[1])
        print("Ваш результат: ", subtraction(a, b))
    elif "*" in res:
        r = int(input("Введите кол-во знаков после запятой: "))
        a = float(res.split("*")[0])
        b = float(res.split("*")[1])
        print("Ваш результат: ", multiplication(a, b, r))
    elif "/" in res:
        r = int(input("Введите кол-во знаков после запятой: "))
        a = float(res.split("/")[0])
        b = float(res.split("/")[1])
        print("Ваш результат: ", division(a, b, r))


calc()
