from os.path import exists as exists

def add_task(tasks: list, task: tuple):
    task_number = len(tasks) + 1

    tasks.append((task_number, task[0], task[1]))

    f = open('tasks.csv', 'a', encoding='utf8')
    f.write(f'{task_number};{task[0]};{task[1]}\n')
    f.close()

def edit_task(tasks: list, task_number, new_task: tuple):
    tasks[task_number - 1] = (len(tasks), new_task[0], new_task[1])
    rewrite_tasks(tasks)

def drop_task(tasks: list, task_number):
    tasks.pop(task_number - 1)
    rewrite_tasks(tasks)

def get_task_tuple(line):
    number, name, category = line.split(';')
    return (number, name, category)

def filter_by_category(tasks: list, category):
    return list(filter(lambda t: t[1] == category, tasks))

def print_tasks(tasks: list):
    for task in tasks:
        print(f"{task[0]}:\t{task[1]} - {task[2]}")

def init_tasks() -> list:
    if not exists('tasks.csv'):
        f = open('tasks.csv', 'a', encoding='utf8')
        f.close()

        tasks = []
    else:
        f = open('tasks.csv', 'r', encoding='utf8')

        tasks = list(map(
            get_task_tuple,
            f.readlines()
        ))

        f.close()
    
    return tasks

def rewrite_tasks(tasks):
    f = open('tasks.csv', 'w', encoding='utf8')
    for task in tasks:
        f.write(f'{task[0]};{task[1]};{task[2]}')  
    
    f.close()

def main():
    tasks = init_tasks()
    
    while True:
        print('Выберите действие: ')
        print('A - создать задачу')
        print('U - изменить задачу')
        print('D - удалить задачу')
        print('F - поиск по категории')
        print('L - вывести список задач')
        print('E - выход')
        print()

        action = input('Ваше действие: ')
        print()

        match action:
            case 'A':
                task_name = input('Задача: ')
                task_category = input('Категория: ')
                add_task(tasks, (task_name, task_category))
                print('Задача добавлена!')
            case 'U':
                task_number = int(input('Номер задачи: '))
                task_name = input('Новое имя: ')
                task_category = input('Новая категория: ')
                edit_task(tasks, task_number, (task_number, task_name, task_category))
                print('Задача изменена!')
            case 'D':
                task_number = int(input('Номер задачи: '))
                drop_task(tasks, task_number)
                print('Задача удалена!')
            case 'L':
                print_tasks(tasks)
            case 'F':
                task_category = input('Введите категорию: ')
                filtered = filter_by_category(tasks, task_category)
                print_tasks(filtered)
            case 'E':
                exit()

        print()
        print()
    

if __name__ == "__main__":
    main()