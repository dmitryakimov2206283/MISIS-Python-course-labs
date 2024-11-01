calls = 0

def call():
    global calls
    calls += 1

def reset_calls():
    global calls
    calls = 0

print(f'Счетчик = {calls}')
print('\n' * 2)
print('Возможные действия:')
print('I - инкремент счетчика')
print('R - сброс сетчика')
print('E - выход')
print()

while True:
    char = input('Действие: ')

    print()

    match char:
        case 'I': call()
        case 'R': reset_calls()
        case 'E': exit()
    
    print(f'Счетчик = {calls}')
    print('\n' * 3)