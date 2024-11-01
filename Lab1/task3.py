n = int(input("Введите трехзначное число: "))

if n < 100 or n > 999:
    print("ЧИСЛО НЕ ТРЕХЗНАЧНОЕ!")
    exit()

hundreds = n // 100
tenth = (n % 100) // 10
units = n % 10

sum = hundreds + tenth + units

print("Сумма чисел: ", sum)
