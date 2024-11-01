import random

expend_categories = [
    'Продукты',
    'Транспорт',
    'Развлечения',
    'Медицина',
    'Одежда',
    'Коммунальные платежи'
]

user_expend_by_category = {}

month_income = float(input("Ваш ежемесячный доход (руб): "))
total_expenditure = 0

for ec in expend_categories:
    expenditure = float(input(f"Ваши расходы по статье \"{ec}\" (руб): "))
    user_expend_by_category[ec] = expenditure
    total_expenditure += expenditure

print("-" * 12)
print(f"Всего расходов: {total_expenditure}")

money_remains = month_income - total_expenditure
print(f"Остаток в месяц: {money_remains}")

print()

if money_remains < 0:
    category_to_reduce_expenses = expend_categories[random.randint(0, len(expend_categories))]
    print(f"Вам следует уменьшить расходы по статье \"{category_to_reduce_expenses}\"")
elif money_remains > 0:
    print(f"Продолжайте в том же духе и за год вы накопите {money_remains * 12} руб!")





