cars_count = int(input("Сколько у вас машин: "))
fuel_consump_norms = {
    1: 7,
    2: 14,
    3: 22
}

for i in range(cars_count):
    print()
    print(f"Введите данные для машины {i + 1}")
    print("-" * 12)

    print("Какая у вас машина?")
    print("\t 1 - малолитражка")
    print("\t 2 - средней мощности")
    print("\t 3 - внедорожник")
    print()

    car_type = int(input("Тип вашей машины (циферкой): "))
    distance = float(input("Пройденное расстояние (км): "))
    fuel_spent = float(input("Расход топлива (л): "))

    fuel_consumption = fuel_spent / distance * 100.0 
    norm = fuel_consump_norms[car_type]

    if norm < fuel_consumption:
        print(f"По норме должно быть {norm} л на 100 км, а у вас - {fuel_consumption:.2f} л")
        print("Вам бы сократить расход...")
    else:
        print(f"Ваш расход составил {fuel_consumption:.2f} л на 100 км, а это норма")



