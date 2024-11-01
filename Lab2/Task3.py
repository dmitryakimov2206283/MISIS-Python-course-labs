days_before_ny = int(input("Дней до новго года: "))

while True:
    print(f"Осталось {days_before_ny} дней до Нового года")
    days_before_ny -= 1

    if days_before_ny == 1:
        print("Завтра Новый год!")
        break