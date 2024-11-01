operations = {
    '+': '<n> + <n>',
    '-': '<n> - <n>',
    '*': '<n> * <n>',
    '/': '<n> / <n>'
}

def eval_operation():
    while True:
        operation = input('Введите операцию: ')
        if operation not in operations:
            print('(!) Выбранная операция не найдена')
            continue
        
        break

    arg1 = float(input('Введите аргумент 1: '))
    arg2 = float(input('Введите аргумент 2: '))

    eval_str = operations[operation]
    eval_str = eval_str.replace('<n>', str(arg1), 1)
    eval_str = eval_str.replace('<n>', str(arg2), 1)

    result = eval(eval_str)
    print(f'Результат: {result}')

def add_operation():
    new_oper = input('Операция: ')
    eval_str = input('Реализация (аргументы вводите как <n>): ')
    operations[new_oper] = eval_str

    print('Операция успешно добавлена!')

def main():
    while True:
        print('Выберите действие:')
        print('O - выполнить операцию')
        print('A - добавить операцию')
        print('E - выход')
        print()

        action = input('Ваше действие: ')

        match action:
            case 'O': eval_operation()
            case 'A': add_operation()
            case 'E': exit()

        print('\n' * 2)


if __name__ == '__main__':
    main()