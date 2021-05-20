import datetime as dt

while True:
    print('q to exit')
    born_date_str = input('Дата рождения дд-мм-гггг: ')
    if born_date_str == 'q':
        break
    born_date = dt.datetime.strptime(born_date_str, '%d-%m-%Y')
    now = dt.datetime.now()
    birthday = dt.datetime.strptime(f'{born_date.day}-{born_date.month}-{now.year}', '%d-%m-%Y')
    if now >= birthday:
        age = now.year - born_date.year
    else:
        age = now.year - born_date.year - 1
    print(age)
