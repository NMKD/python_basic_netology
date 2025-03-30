# Задание 4: подбор упаковок по размерам товара
width = 50
length = 50
height = 10

if width <= 15 and length <= 15 and height <= 15:
    print('Коробка №1')
elif width > 200 or length > 200 or height > 200:
    print('Упаковка для лыж')
elif 50 > width > 15 or 50 > length > 15 or 50 > height > 15:
    print('Коробка №2')
else:
    print('Коробка №3')
