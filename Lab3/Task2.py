def sort_list(list, desc = False):
    return sorted(list, key=lambda student: student[1], reverse=desc)

students = [
    ('Алиса', 85),
    ('Дима', 75),
    ('Андрей', 98),
    ('Петя', 72),
    ('Юля', 64)
]

print(f'Список до сортировки: {students}')
print(f'Сортировка по возрастанию: {sort_list(students)}')
print(f'Сортировка по убыванию: {sort_list(students, True)}')