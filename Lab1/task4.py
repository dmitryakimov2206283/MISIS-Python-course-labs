n = int(input("Введите число n (n <= 1000): "))

if n > 1000:
    print("ЧИСЛО НЕ ДОЛЖНО ПРЕВЫШАТЬ 1000!")
    exit()

n += n % 2

print("Следующее четное число: ", n)