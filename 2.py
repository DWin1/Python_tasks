#секунды в часы, минуты, секунды

time_sec = int(input('Введите время в секундах'))
time_hour = time_sec // 3600
time_min = (time_sec % 3600) // 60
time_sec = time_sec - (time_hour * 3600) - (time_min * 60)
print (f"Ваши секунды в формате ЧЧ:ММ:СС {time_hour}:{time_min}:{time_sec}")