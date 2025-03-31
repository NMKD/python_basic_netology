"""
  Запрашивает у пользователя числа, пока не будет введен 0,
  и выводит сумму всех введенных чисел до 0.
"""
# Вариант 1
# number = ''
# sum_of_numbers = 0
# while number != 0:
#     number = int(input())
#     sum_of_numbers += number


# print(sum_of_numbers)

# Вариант 1
total_sum = 0
while True:
    try:
        num = int(input("Введите число: "))
        if num == 0:
            break
        else:
            total_sum += num
    except ValueError:
        print("Ошибка: Пожалуйста, введите целое число.")
print(f'Результат: {total_sum}')
