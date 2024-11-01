def dish_filter(dish):
	if dish[1] <= budget:
		return True
		
	return False

def find_affordable(dishes: list):
	return list(filter(dish_filter, dishes))
	
def add_or_update_dish(dishes: list, name, price):

	if (name, price) not in dishes:
		dishes.append((name, price))
		return

	dish = next(
		filter(
			lambda d: True if d[0] == name else False,
			dishes
		),
		None
	)

	if dish is None:
		return
	
	index = dishes.index(dish)
	dishes[index] = (name, price)

dishes = [
	('Пельмени', 200.0),
	('Шаурма', 250.0),
	('Сухарики', 70.0)
]

while True:	
	print('Выберите действие:')
	print('1 - найти, что могу купить')
	print('2 - добавить/обновить стоимость блюда')
	print('E - выход')
	print()

	action = input('Ваше действие: ')

	match action:
		case '1':
			budget = float(input('Ваш бюджет: '))
			affordable = find_affordable(dishes)	
			print(f'Вы можете позволить: {affordable}')
		case '2':
			dish_name = input('Название блюда: ')
			price = float(input('Цена: '))
			add_or_update_dish(dishes, dish_name, price)
			print(f'Блюдо "{dish_name}" внесено!')
			print(dishes)
		case 'E':
			exit()
	
	print()
	print()

	

	