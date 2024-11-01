lines = []

def print_file_contents(file, title):
    f = open(file, 'r', encoding='utf-8')

    global lines
    lines = f.readlines()

    print(title)
    print('-' * 12)
    print()

    for line in lines:
        print(line)

    f.close()

print_file_contents('words.txt', 'Исходный файл:')

f = open('words_reversed.txt', 'w', encoding='utf-8')

for line in reversed(lines):
    f.write(line)

f.close()

print('\n' * 3)

print_file_contents('words_reversed.txt', 'Файл в обратном порядке:')

