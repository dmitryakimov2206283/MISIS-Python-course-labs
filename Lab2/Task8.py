from random import shuffle

num_list = list(map(int, 
    input("Введите 5 чисел через пробел: ").split(" ")))

if len(num_list) != 5:
    print("Надо было ввести ровно 5 чисел...")

print(f"Введенный список: {num_list}")
shuffle(num_list)
print(f"Перемешанный список: {num_list}")

min_num = num_list[0]
max_num = num_list[0]

for n in num_list:
    if n < min_num:
        min_num = n
    elif n > max_num:
        max_num = n

print(f"Минимум: {min_num}")
print(f"Максимум: {max_num}")