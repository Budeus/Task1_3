# Дано целое положительное число X, необходимо вывести вариант этого числа в римской системе счисления в формате строки.
# Римские числа записываются от наибольшего числа к наименьшему слева направо.
# Однако число 4 не является “IIII”. Вместо этого число 4 записывается, как “IV”. Т.к. 1 стоит перед 5, мы вычитаем 1, делая 4. Тот же принцип применим к числу 9, которое записывается как “IX”.
# Случаи, когда используется вычитание:
# I может быть помещен перед V и X, чтобы сделать 4 и 9.
# X может быть помещен перед L и C, чтобы составить 40 и 90.
# C может быть помещен перед D и M, чтобы составить 400 и 900.

# Пример 1:
# Ввод: x = 3
# Вывод: “III”
# Пример 2:
# Ввод: x = 9
# Вывод: “IX”
# Пример 3:
# Ввод: x = 1945
# Вывод: “MCMXLV”
# Гарантируется, что введенное число X будет находиться в диапазоне от 1 до 2000


print('Введите число в арабской системе от 1 до 2000')
arab_digits = input()
#print(len(arab_digits))
dict_thousands = dict(([1, 2],['M', 'MM']))
dict_hundreds = dict(zip(['C', 'CC', 'CCC', 'CD', 'D', 'DI', 'DII', 'DIII','CM', ''], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
dict_tens = dict(zip(['X', 'XX', 'XXX', 'XL', 'L', 'LI', 'LII', 'LIII','XC', ''], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
dict_digits = dict(zip(['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII','IX', 'X'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

rome_thousands = dict_thousands(int(arab_digits[0]))
print(rome_thousands)

# for i in range(0,len(arab_digits)):
#     if i == 0:
#         rome_thousands = dict_thousands(arab_digits[i])        
#     print(rome_thousands)
    
#     if i == 1:
#         rome_hundreds = dict_hundreds(arab_digits[i])        
#     print(rome_hundreds)

#     if i == 2:
#         rome_tens = dict_tens(arab_digits[i])        
#     print(rome_tens)

#     if i == 3:
#         rome_digits = dict_digits(arab_digits[i])        
#     print(rome_digits)

# print(rome_thousands, rome_hundreds, rome_tens, rome_digits)


# for i in range(0,len(arab_digits)):
#     print(arab_digits[i])
#my_dict = dict(zip(['I', 'II', 'III', 'IV', 'V', 'VI', 'VII',], [1, 2, 3]))  
#my_value = my_dict['key']

# for digit in len(arab_digits):
#     if len(arab_digits) == 4:
