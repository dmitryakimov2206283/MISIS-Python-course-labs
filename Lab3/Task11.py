
def find_product_min_max():
    f = open('products.csv', 'r', encoding='utf8')
    lines = f.readlines()
    f.close()

    products = {}

    max_name = ''
    min_name = ''

    for line in lines:
        name, count, price = line.split('\t')
        cost = float(price) * int(count)
        products[name] = cost

        if max_name == '':
            max_name = name
        elif products[max_name] < cost:
            max_name = name

        if min_name == '':
            min_name = name
        elif products[min_name] > cost:
            min_name = name
    
    print('Сумма продаж:')
    for name, cost in products.items():
        print(f'Товар "{name}" всего стоит {cost} руб.')
    
    print()

    print(f'Макс. стоимость у {max_name} ({products[max_name]} руб.)')
    print(f'Мин. стоимость у {min_name} ({products[min_name]} руб.)')

def add_product():
    name = input('Продукт: ')
    price = input('С ценой: ')
    count = input('В количестве: ')

    f = open('products.csv', 'a', encoding='utf8')
    f.write(f'\n{name}\t{count}\t{price}')
    f.close()

    print()
    print(f'Товар "{name}" успешно добавлен!')

def main():
    while True:
        print('Выберите действие:')
        print('F - экстремумы продаж')
        print('A - добавить продукт')
        print('E - выход')
        print()

        action = input('Ваше действие: ')

        match action:
            case 'F': find_product_min_max()
            case 'A': add_product()
            case 'E': exit()

        print('\n' * 3)

if __name__ == "__main__":
    main()