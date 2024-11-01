# Список значений температуры
temp_list = list(map(int, 
    input("Введите 7 значений температуры (через пробел): ").split(" ")))

list_len = len(temp_list)

if len(temp_list) != 7:
    print(f"Введено {list_len} значений")
    print("А надо было ввести 7...")

avg_temp = 0
min_temp = temp_list[0]
max_temp = temp_list[0]

for t in temp_list:
    avg_temp += t
    if (t < min_temp):
        min_temp = t
    elif (t > max_temp):
        max_temp = t

avg_temp = avg_temp / list_len

clothes_str = ""

if avg_temp < 0:
    clothes_str = "зимнюю одежду"
elif avg_temp >= 0 and avg_temp < 10:
    clothes_str = "осеннюю одежду"
elif avg_temp >= 10 and avg_temp < 20:
    clothes_str = "весеннюю одежду"
else:
    clothes_str = "летнюю одежду"

print(f"Макс. и мин. температура {max_temp}°С и {min_temp}°С соответственно")
print(f"Среднесуточная температура составила {avg_temp}°С - носите {clothes_str}")
