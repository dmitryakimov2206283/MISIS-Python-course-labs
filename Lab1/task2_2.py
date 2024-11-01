n = int(input("Введите число n: "))

if n > 10**7:
    print("Число не может превышать 10^7")
    exit()

secs_in_day = 86400
secs_remain = n % secs_in_day

hours = secs_remain // 3600
minutes = secs_remain % 3600 // 60
seconds = secs_remain % 3600 % 60

pretty_minutes = str(minutes).zfill(2)
pretty_seconds = str(seconds).zfill(2)

print(f"{hours}:{pretty_minutes}:{pretty_seconds}")



# n = seconds + 60 * minutes + 3600 * hours