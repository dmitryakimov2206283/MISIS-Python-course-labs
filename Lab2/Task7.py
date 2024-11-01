words = input("Введите строку текста: ").split(" ")

chr_count = len(words)
print(f"Всего символов: {chr_count}")

vowels = {'а', 'о', 'у', 'ы', 'э', 'е', 'и', 'я', 'ё', 'ю',
          'a', 'e', 'i', 'o', 'u', 'y'}

vowels_count = 0
unique_words = set()
duplicates = list()

for word in words:
    for c in word:
        if c.lower() in vowels:
            vowels_count += 1

    if word in unique_words:
        duplicates.append(word)
    else:
        unique_words.add(word)

print(f"Всего гласных: {vowels_count}")
print()

print("Слова текста:")
print("-" * 12)

for u in unique_words:
    print(u)

print()
print("Убранные дубликаты:")
print("-" * 12)

for d in duplicates:
    print(d)