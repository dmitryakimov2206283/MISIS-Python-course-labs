string = input("Введите строку: ")

chunks = []
for c in string:
    if c.isspace():
        chunks.append(c)
    else:
        chunks.append(
            chr(ord(c) + 1)
        )

encrypted = "".join(chunks)
print(f"Зашифрованная строка: {encrypted}")