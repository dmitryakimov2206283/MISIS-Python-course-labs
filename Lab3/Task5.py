currency_course = {
	'USD': 75,
	'EUR': 90
}

def convert_currency(rubs, currency):
	return rubs / currency_course[currency]
	
def update_course(currency, new_value):
	currency_course[currency] = new_value
	
def drop_course(currency):
	currency_course.pop(currency, None)

while True:
	print('Выберите действие:')
	print('1 - Конвертировать')
	print('2 - Добавить/Обновить курс')
	print('3 - Удалить курс')
	print('E - Выход')
	print()
	action = input('Ваше действие: ')
	
	match action:
		case '1':
			rubs = float(input('Введите рубли: '))

			print(f'Доступные курсы: {currency_course}')
			currency = input('Введите валюту: ')
			
			converted = convert_currency(rubs, currency)
			print(f'Рубли в {currency}: {converted:.2f}')
		case '2':
			currency = input('Валюта: ')
			value = float(input('Курс: '))
			update_course(currency, value)
			print(f'Курс для {currency} добавлен!')
			print(currency_course)
		case '3':
			print(f'Доступные курсы: {currency_course}')
			currency = input('Валюта: ')
			drop_course(currency)
			print(f'Курс для {currency} удален!')
			print(currency_course)
		case 'E':
			exit()
			
	print()
	
	
