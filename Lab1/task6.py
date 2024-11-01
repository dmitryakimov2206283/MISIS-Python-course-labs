line = input("Введите 4 целых числа через пробел: ")

values = line.split(" ")
val_count = len(values)

if val_count > 4:
    print("КОЛИЧЕСТВО ЧИСЕЛ БОЛЬШЕ 4-Х!")
    exit()

sum = 0
for i in range(val_count):
    sum += int(values[i])

avg = sum / val_count

print("Сред. арифметическое: ", avg)