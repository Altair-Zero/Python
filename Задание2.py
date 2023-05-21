
stroka = str(input("Введите строку: "))
c = 0
length = len(stroka)
newstroka = str()

for i in range(length):
    if (i == 2):     # пропустить 3-й символ
        continue

    if (stroka[i] == 'с'):
        c += 1              # Проверка на наличие символа с и его количества
        print(f"В строке есть символ 'с'. {c}.")  

    newstroka += stroka[i]  

    if (i + 1 == length):   # вывод строки без последнего символа
        print(newstroka[:-1])

print(f"Длина строки равна = {len(stroka)}")
