
age = int(input("Ваш возраст: "))

if age < 18:
    print("Доступ запрещен")
elif age >= 18 and age <= 25:
    print("Добро пожаловать молодой гость")
elif age > 25 and age <= 60:
    print("Добро пожаловать в клуб")
else:
    print("Будьте осторожны, пожалуйста")