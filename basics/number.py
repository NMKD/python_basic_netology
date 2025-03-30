# Задание 5: Счастливый билет
string_to_number_to_sum = str(123321)
# input_string = input()
if len(string_to_number_to_sum) == 6:
    sum_first_half = int(string_to_number_to_sum[0]) + int(
        string_to_number_to_sum[1]) + int(string_to_number_to_sum[2])
    sum_second_half = int(string_to_number_to_sum[3]) + int(
        string_to_number_to_sum[4]) + int(string_to_number_to_sum[5])
    if sum_first_half == sum_second_half:
        print('Счастливый билет')
    else:
        print('Несчастливый билет')
else:
    print('Введите число равное 6 символом')
