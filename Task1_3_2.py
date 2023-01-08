print('Введите строку на проверку, является или она палиндромом')

str_X = input().lower()
str_X1 = str_X.replace(" ", "").lower()
str_Y = str_X1[::-1].lower()

print("True" if str_X1 == str_Y else "False")