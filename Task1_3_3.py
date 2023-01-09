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


print('Введите число в арабской системе счисления от 1 до 2000')
arab_digits1 = input()
arab_digits = arab_digits1[::-1]

dict_thousands = {1:'M', 2:'MM'}
dict_hundreds = {1:'C', 2:'CC', 3:'CCC', 4:'CD', 5:'D', 6:'DI', 7:'DII', 8:'DIII', 9:'CM', 0:''}
dict_tens = {1:'X', 2:'XX', 3:'XXX', 4:'XL', 5:'L', 6:'LI', 7:'LII', 8:'LIII', 9:'XC', 0:''}
dict_digits = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX', 0:''}

rome_tens = ""
rome_digits = ""
rome_hundreds = ""
rome_thousands = ""

for i in range(0,len(arab_digits)):
    if i == 0:
        rome_digits = dict_digits[int(arab_digits[i])]                     
    elif i == 1:
        rome_tens = dict_tens[int(arab_digits[i])]        
    elif i == 2:
        rome_hundreds = dict_hundreds[int(arab_digits[i])]
    elif i == 3:
        rome_thousands = dict_thousands[int(arab_digits[i])]        

print('Число в римской системе счисления - ', rome_thousands + rome_hundreds + rome_tens + rome_digits)