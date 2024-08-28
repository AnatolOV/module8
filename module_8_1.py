def add_everything_up(a, b):
    try:
        return a + b
    except TypeError as exc:
        a = f'{a}'
        b = f'{b}'
        # print(f'ошибка: {exc}')
        return a + b


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))