#5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.

salary = int(input('Введите доход фирмы '))
costs = int(input('Введите доход фирмы '))
if salary > costs:
    print('Вы работаете с доходом')
elif salary == costs:
    print('Вы держитесь на плаву')
else:
    print('Вы работаете с убытком')