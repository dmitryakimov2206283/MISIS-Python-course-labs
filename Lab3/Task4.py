def get_discounts(prices, discount_formula):
    return discount_formula(prices)

prices = list(map(float, input('Введите список цен (через пробел): ').split()))
print()

print('Возможные скидки:')
print('1 - 10%')
print('2 - 20%')
print('3 - 30%')
print('E - выход')
print('')

discount_type = input('Выбранный тип: ')

match discount_type:
    case '1': discount_formula = lambda l: [li - (li * 0.1) for li in l]
    case '2': discount_formula = lambda l: [li - (li * 0.2) for li in l]
    case '3': discount_formula = lambda l: [li - (li * 0.3) for li in l]
    case 'E': exit()

print(get_discounts(prices, discount_formula))