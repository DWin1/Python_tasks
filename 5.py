#5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.

doxod = int(input('Введите доход фирмы '))
izder = int(input('Введите доход фирмы '))
if doxod > izder:
    print('Вы работаете с доходом')
elif doxod == izder:
    print('Вы держитесь на плаву')
else:
    print('Вы работаете с убытком')