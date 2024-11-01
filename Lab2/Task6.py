password = input("Введите пароль: ")

# Длина должна быть не менее 8 символов
pass_len_cr = False if len(password) < 8 else True
# Пароль должен содержать хотя бы одну цифру
pass_num_cr = False
# Пароль должен содержать хотя бы одну заглавную букву
pass_upper_cr = False
# Пароль должен содержать хотя бы один специальный символ
pass_spceial_cr = False

for c in password:
    if c.isdigit():
        pass_num_cr = True
    
    if c.isupper():
        pass_upper_cr = True
    
    if not c.isalnum():
        pass_spceial_cr = True

if not pass_num_cr:
    print("Пароль должен содержать хотя бы одну цифру!")

if not pass_upper_cr:
    print("Пароль должен содержать хотя бы одну заглавную букву!")

if not pass_spceial_cr:
    print("Пароль должен содержать хотя бы один специальный символ!")

if (pass_len_cr
    and pass_num_cr
    and pass_upper_cr
    and pass_spceial_cr):
    print("Пароль подходящий!")