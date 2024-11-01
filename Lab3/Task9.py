def print_product_price(products: dict, name):
    print(f'Цена для {name} составляет {products[name]:.2f} руб.')

def add_or_update_price(products: dict, name, price):
    products[name] = price

def drop_product(products: dict, name):
    products.pop(name)

def print_product_list(products: dict):
    print('Текущий список продуктов:')
    for name, price in products.items():
        print(f'"{name}" стоит {price:.2f} руб.')

def main():
    print('Сейчас вам будет предложено ввести список продуктов.')
    print('Формат ввода: <продукт1>,<цена1> <продукт2>,<цена2> ...')
    print()

    product_data = list(input('Список продуктов: ').split())

    products = {}

    print()
    print()

    for p in product_data:
        name, price = p.split(',')
        products[name] = float(price)
    
    while True:
        print('Выберите действие')
        print('F - найти цену продукта')
        print('A - добавить/обновить цену продукта')
        print('D - удалить продукт из списка')
        print('L - вывести список продуктов')
        print('E - выход')
        print()

        action = input('Ваше действие: ')

        match action:
            case 'F':
                product_name = input('Название продукта: ')
                print_product_price(products, product_name)
            case 'A':
                product_name = input('Название продукта: ')
                price = float(input('Его цена: '))
                add_or_update_price(products, product_name, price)

                print(f'Цена для {product_name} внесена')
            case 'D':
                product_name = input('Название продукта: ')
                drop_product(products, product_name)

                print(f'Продукт "{product_name}" удален!')
            case 'L':
                print_product_list(products)
            case 'E':
                exit()
        
        print()
        print()

if __name__ == '__main__':
    main()