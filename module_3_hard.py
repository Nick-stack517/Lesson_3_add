# Задача: найти решение для подсчета суммы всех чисел и длин всех строк.
# Что должно быть подсчитано:
# Все числа (не важно, являются они ключами или значениям или ещё чем-то).
# Все строки (не важно, являются они ключами или значениям или ещё чем-то)


def sum_num_len(data_in):
    summa = 0
    if isinstance(data_in, (list, tuple, set)):
        for element in data_in:
            summa += sum_num_len(element)

    elif isinstance(data_in, dict):
        for key, value in data_in.items():
            summa += sum_num_len(key)
            summa += sum_num_len(value)

    elif isinstance(data_in, (int, float)):
        summa += data_in

    elif isinstance(data_in, str):
        summa += len(data_in)

    return summa


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = sum_num_len(data_structure)
print(result)
