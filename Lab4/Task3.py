class User:
    def __init__(self, user_id, name, email, age):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.age = age

    def __str__(self):
        return f"{self.user_id}, {self.name}, {self.email}, {self.age}"
    
    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "age": self.age
        }
    
class FileManager:
    FILE_NAME = "users.txt"

    @staticmethod
    def load_users():
        f = open(FileManager.FILE_NAME, 'r', encoding='utf8')

        users = []

        for line in f:
            ud = line[1:len(line) - 2]
            ud = ud.split(',')

            user_id = ud[0].split(':')[1].strip().replace("'", "")
            name = ud[1].split(':')[1].strip().replace("'", "")
            email = ud[2].split(':')[1].strip().replace("'", "")
            age = ud[3].split(':')[1].strip().replace("'", "")
            users.append(User(user_id, name, email, age))

        f.close()

        return users

    @staticmethod
    def save_users(users):
        f = open(FileManager.FILE_NAME, 'w', encoding='utf8')
        for u in users:
            f.write(str(u.to_dict()) + "\n")
        f.close()

    @staticmethod
    def add_user(user):
        f = open(FileManager.FILE_NAME, 'a', encoding='utf8')
        f.write(str(user.to_dict()) + "\n")
        f.close()        


def add_user(users_count):
    user_id = users_count + 1
    name = input('Введите имя: ')
    email = input('Введите email: ')
    age = input('Введите возраст: ')

    FileManager.add_user(User(user_id, name, email, age))

    print('Пользователь добавлен.')

def update_user(users: list):
    user_id = input("Введите ID пользователя для изменения: ")

    user = None
    for u in users:
        if u.user_id == user_id:
            user = u
            break
    
    user.name = input('Введите новое имя: ')
    user.email = input('Введите новый email: ')
    user.age = input('Введите новый возраст: ')

    FileManager.save_users(users)

    print('Пользователь изменен.')

def delete_user(users: list):
    user_id = input("Введите ID пользователя для изменения: ")

    user = None
    for u in users:
        if u.user_id == user_id:
            user = u
            break

    users.remove(user)

    FileManager.save_users(users)

    print('Пользователь удален.')

def print_users(users: list):
    for u in users:
        print(u)

def main():
    users = FileManager.load_users()

    while True:
        print('Выберите действия:')
        print('A - добавить пользователя')
        print('U - отредактировать пользователя')
        print('L - просмотр списка пользователей')
        print('D - удалить пользователя')
        print('E - выход')

        action = input('Ваше действие: ')

        match action:
            case 'A': 
                add_user(len(users))
                users = FileManager.load_users()
            case 'U': update_user(users)
            case 'L': print_users(users)
            case 'D': delete_user(users)
            case 'E': exit()

        print('\n' * 2)

if __name__ == "__main__":
    main()
