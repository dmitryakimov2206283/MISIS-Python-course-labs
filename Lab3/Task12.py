word = input('Найти слово: ')
case_sensitive = True if input('Учитывать регистр? [y/n]: ') == 'y' else False

if not case_sensitive:
    word = word.lower()

f = open('words.txt', 'r', encoding='utf-8')
lines = f.readlines()

print()
print('Найденные вхождения:')
print('-' * 12)
print()

occurences_num = 0

for line in lines:
    if not case_sensitive:
        line = line.lower()

    if line.find(word) != -1:
        occurences_num += 1
        print(line)

f.close()

print()
print(f'Всего вхождений: {occurences_num}')