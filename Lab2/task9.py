import os 
import platform

sysname = platform.system()
cls = None

if sysname == "Windows":
    cls = lambda: os.system('cls')
else:
    cls = lambda: os.system('clear')

tasks = []

print("Заполните список задач (нужно ввести 5 задач)")
print("-" * 12)

for i in range(5):
    tasks.append(input(f"Введите задачу №{i + 1}: "))

cls()

while len(tasks) != 0:
    print("Какую задачу выполним?")
    print("-" * 12)
    for i in range(len(tasks)):
        print(f"[{i + 1}] {tasks[i]}")

    print()
    task_to_complete = int(input("Введите номер задачи: "))
    tasks.pop(task_to_complete - 1)
    cls()

print("Все задачи выполнены!")



