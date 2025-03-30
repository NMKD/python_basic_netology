# Задание 3: Знаки зодиака
day = int(input("Введите day:\n"))
month = input("Введите month:\n").lower()  # Приводим к нижнему регистру

if month == "январь":
    if day <= 19:
        sign = "Козерог"
    else:
        sign = "Водолей"
elif month == "февраль":
    if day <= 18:
        sign = "Водолей"
    else:
        sign = "Рыбы"
elif month == "март":
    if day <= 20:
        sign = "Рыбы"
    else:
        sign = "Овен"
elif month == "апрель":
    if day <= 19:
        sign = "Овен"
    else:
        sign = "Телец"
elif month == "май":
    if day <= 20:
        sign = "Телец"
    else:
        sign = "Близнецы"
elif month == "июнь":
    if day <= 20:
        sign = "Близнецы"
    else:
        sign = "Рак"
elif month == "июль":
    if day <= 22:
        sign = "Рак"
    else:
        sign = "Лев"
elif month == "август":
    if day <= 22:
        sign = "Лев"
    else:
        sign = "Дева"
elif month == "сентябрь":
    if day <= 22:
        sign = "Дева"
    else:
        sign = "Весы"
elif month == "октябрь":
    if day <= 22:
        sign = "Весы"
    else:
        sign = "Скорпион"
elif month == "ноябрь":
    if day <= 21:
        sign = "Скорпион"
    else:
        sign = "Стрелец"
elif month == "декабрь":
    if day <= 21:
        sign = "Стрелец"
    else:
        sign = "Козерог"
else:
    sign = "Некорректный ввод месяца"

print("Ваш знак зодиака:", sign)
