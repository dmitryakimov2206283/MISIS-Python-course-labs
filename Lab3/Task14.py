import pandas as pd

def print_mean():
    csv = pd.read_csv('students.csv')
    mean = round(csv.iloc[:, 1].mean(), 3)
    low_rating_stud = csv[csv['Оценка'] < mean]

    print(f'Средний балл: {mean}')
    print()
    print('Оценка ниже среднего у:')
    print(low_rating_stud)

def add_student():
    name = input('Студент: ')
    score = input('Оценка: ')
    recalc = True if input('Пересчитать средний балл? [y/n]: ') == 'y' else False

    new_student = pd.DataFrame({
        'Студент': [name],
        'Оценка': [score]
    })

    new_student.to_csv('students.csv', mode='a', index=False, header=False)

    if recalc:
        print_mean()

def main():
    while True:
        print('Выберите действие: ')
        print('M - вывести средний балл')
        print('A - добавить студента')
        print('E - выход')
        print()

        action = input('Ваше действие: ')

        match action:
            case 'M': print_mean()
            case 'A': add_student()
            case 'E': exit()

        print('\n' * 2)

if __name__ == '__main__':
    main()
