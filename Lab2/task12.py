weekdays = {
    1: "Пн",
    2: "Вт",
    3: "Ср",
    4: "Чт",
    5: "Пт",
    6: "Сб",
    7: "Вс"
}

steps_per_day = []

# Дни, когда пользователь прошел более 10 000 шагов
lucky_days = []

print("Узнаем ваши шаги за неделю")
print("-" * 12)

steps_count = 0
total_steps = 0

for i in range(1, 8):
    steps_count = int(input(f"Кол-во шагов в {weekdays[i]}: "))

    if (steps_count >= 10000):
        lucky_days.append(i)

    steps_per_day.append(steps_count)
    total_steps += steps_count

avg_steps = total_steps / 7

print()
print("Итого, за эту неделю")
print("-" * 12)
print(f"Вы прошли {total_steps} шагов и сожгли {total_steps * 0.05:.2f} калорий")
print(f"В {', '.join([weekdays[ld] for ld in lucky_days])} вы прошли более 10 000 шагов! Поздравляем!" )
