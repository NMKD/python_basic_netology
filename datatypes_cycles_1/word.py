# Задание 1: выводи среднюю букву, если число букв в слове нечетное или
# две средних буквы, если число букв четное.
word = 'testing'
len_of_word = len(word)
if len_of_word % 2 == 0:
    # print(type(len_of_word // 2))
    print(word[len_of_word // 2] + word[len_of_word // 2 - 1])
else:
    print(word[len_of_word // 2])
