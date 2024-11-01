import datetime
import string


def log(message):
    current_date = datetime.date.today()

    f = open('errors.log', 'a', encoding='utf8')
    f.write(f'[{current_date}]\t{message}\n')

    f.close()

def gen_errors():
    try:
        num = int(input('Введите целое число: '))
    except ValueError as ve:
        log('Значение  не является целым числом')

    try:
        fnum = float(input('Введите число с плавающей запятой: '))
    except ValueError as ve:
        log('Значение  не является числом с плавающей точкой')

    try:
        vals = input('Введите значения через запятую: ')
        for ch in vals:
            if (ch in string.punctuation) and (ch != ',' and ch != ' '):
                raise Exception('Неверный формат данных (данные должны быть введены через запятую)')
    except Exception as e:
        log(e)

def print_top_logs(top):
    try:
        f = open('errors.log', 'r', encoding='utf8')

        for _ in range(top):
            print(f.readline())

        f.close()
    except FileNotFoundError as fne:
        log(fne)

def main():
    while True:
        print('Выберите действие: ')
        print('G - генерация ошибок ввода')
        print('P - вывод логов ошибок')
        print('E - выход')
        print()

        action = input('Ваше действие: ')

        match action:
            case 'G': gen_errors()
            case 'P': print_top_logs(5)
            case 'E': exit()

        print('\n' * 2)

if __name__ == '__main__':
    main()