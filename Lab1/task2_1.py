n = int(input("Введите число n: "))

if n > 10**7:
    print("Число не может превышать 10^7")
    exit()

mins_in_day = 1440
mins_remain = n % mins_in_day

hours = mins_remain // 60
minutes = mins_remain % 60

pretty_minutes = str(minutes).zfill(2)

print(f"{hours}:{pretty_minutes}")