from math import ceil

N = int(input("Количество человек: "))

cars_count = ceil(N / 4)

print("Понадобиться машин: ", cars_count)