# Дана строка X, состоящая только из символов “{“, “}”, “[“, “]”, “(“, “)”. Программа должна вывести True, в том случае если все открытые скобки закрыты. Например: “[()]{}”, все открытые скобки закрыты закрывающимися скобками, потому вывод будет True. В случае же, если строка будет похожа на: “{{{}”, то вывод будет False, т.к. не все открытые скобки закрыты.

# Пример 1:
# Ввод: x = “[{}({})]”
# Вывод: True
# Пример 2:
# Ввод: x = “{]”
# Вывод: False
# Пример 3:
# Ввод: x = “{“
# Вывод: False
# Гарантируется, что введенная строка X будет содержать только скобки и не будет пустой.


print('Введите строку из символов “{“, “}”, “[“, “]”, “(“, “)”')
symbols = input()
#print(len(arab_digits))
control = False
counter11 = 0
counter12 = 0
counter21 = 0
counter22 = 0
counter31 = 0
counter32 = 0

for i in range(0, len(symbols)):
    if symbols[i]=="{":
        counter11 = counter11 + 1
    if symbols[i]=="}":
        counter12 = counter12 + 1

    if symbols[i]=="[":
        counter21 = counter21 + 1
    if symbols[i]=="]":
        counter22 = counter22 + 1

    if symbols[i]==")":
        counter31 = counter31 + 1
    if symbols[i]=="(":
        counter32 = counter32 + 1

if (counter11 == counter12) and (counter21 == counter22) and (counter31 == counter32):
    control = True

print("True" if control == True else "False")