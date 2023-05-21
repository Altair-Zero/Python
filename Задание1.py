
num = float(input("Введите произвольное число: "))
limit = float(input("Введите пограничное число: "))

if num < limit:
    print(f"{num} меньше, чем пограничное число {limit}")
elif num > limit:
    print(f"{num} больше, чем пограничное число {limit}")
    if num > num * 3:
        print(f"{num} больше, чем пограничное число {limit} более, чем в 3 раза")
else:
    print(f"{num} равно пограничному числу {limit}")
