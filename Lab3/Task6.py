def drop_user_duplicates(users):
	users_set = set()
	
	for user in users:
		if user in users_set:
			print(f'Дубликат: {user}')
		else:
			users_set.add(user)
	
	return list(users_set)

while True:	
	users = list(input('Пользователи (через пробел): ').split())

	no_duplicates = drop_user_duplicates(users)
	print(f'Список без дубликатов: {no_duplicates}')
	print()