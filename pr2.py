import random
users = [
    {
        'username': 'Twelve',
        'password': '12345',
        'role': 'user',
        'history': [],
        'created_at': '2024-12-01'
    },
    {
        'username': 'admin111',
        'password': '54321',
        'role': 'admin'
    },
]
rooms = [
    {'title': 'superior', 'price': 3500},
    {'title': 'double', 'price': 1500},
    {'title': 'suite', 'price': 5000},
    {'title': 'family room', 'price': 3000},
    {'title': 'single', 'price': 1000},
]


def f(r, login):
    ot = input("от какой суммы? ")
    while not ot.isdigit():
        ot = input("Ввести можно только числа! ")
    do = input("до какой суммы? ")
    while not do.isdigit():
        do = input("Ввести можно только числа! ")
    ot, do = int(ot), int(do)
    result = list(filter(lambda x: do >= x['price'] >= ot, r))
    for var in result:
        print(f'Название номера: {var["title"]}, цена: {var["price"]} за ночь')
    menu_user(r, login)


def ssort(r, login):
    cho = input("Чтобы отсортировать по возрастанию цены, введите 'возр'. Или 'убыв', если по убыванию': ")
    while cho not in 'возрубыв':
        cho = input("Ввести можно только 'возр' или 'убыв': ")
    if cho == 'возр':
        sortlist = sorted(r, key=lambda x: x['price'])
        for i in sortlist:
            print(f'Название номера: {i["title"]}, цена: {i["price"]} за ночь')
    else:
        sortlist = sorted(r, key=lambda x: x['price'], reverse=True)
        for i in sortlist:
            print(f'Название номера: {i["title"]}, цена: {i["price"]} за ночь')
    menu_user(r, login)


def menu_user(r, login):
    global rate
    print('-----------------------------------------------------')
    print('Выберите действие:\n1. Просмотреть каталог номеров\n2. Найти номер и снять\n3. Сортировать номера по цене\n4. Выйти'
          '\n5. Отфильтровать по цене\n6. Просмотр истории покупок\n7. Обновить профиль')
    print('-----------------------------------------------------')
    answer = input()
    if answer not in '1234567':
        while answer not in '1234567':
            answer = input('Такого действия нет! Попробуйте еще раз: ')
    match answer:
        case '1':
            for i in r:
                print(f'Название номера: {i["title"]}, цена: {i["price"]} за ночь')
            menu_user(r, login)
        case '4':
            start(r)
        case '5':
            f(r, login)
        case '3':
            ssort(r, login)
        case '6':
            for i in users:
                if i['username'] == login:
                    if not i['history']:
                        print('История покупок пуста')
                        menu_user(r, login)
                        break
                    else:
                        print("Вы снимали номера: ", end='')
                        print(*i['history'], sep=', ')
                        menu_user(r, login)
                        break
        case '2':
            room = input("Введите название номера: ")
            nomera = []
            for i in rooms:
                nomera.append(i['title'])
            while room not in nomera:
                room = input("Номера с таким названием не существует! ")
            days = input(f"На сколько дней вы хотите снять номер '{room}' (от 1 до 14)? ")
            while not days.isdigit():
                days = input("Ввести нужно число! ")
            days = int(days)
            while not 1 <= days <= 14:
                days = input("Снять номер можно от 1 до 14 дней! ")
                while not days.isdigit():
                    days = input("Ввести нужно число! ")
                days = int(days)
            for i in rooms:
                if room == i['title']:
                    rate = i['price']
                    break
            purchase = input(f"Введите 'да', если готовы снять номер '{room}' на {days} суток за {rate * days} рублей,"
                             f" и 'нет', если не готовы? ")
            while purchase != 'да' and purchase != 'нет':
                purchase = input("Можно ввести только 'да' или 'нет': ")
            if purchase == 'да':
                print(f"Поздравляем с покупкой. Вам номерок {random.randint(1, 350)}")
                for i in users:
                    if i['username'] == login:
                        i['history'].append(room)
                menu_user(r, login)
            else:
                print("Вы отменили покупку.")
                menu_user(r, login)
        case '7':
            change = input("Что вы хотите поменять? Введите 'логин' или 'пароль': ")
            while change != 'логин' and change != 'пароль':
                change = input("Ввести можно только 'логин' или 'пароль'! ")
            if change == 'логин':
                new_login = input('Введите новый логин: ')
                for i in users:
                    if i['username'] == login:
                        i['username'] = new_login
                        break
                print('логин изменен')
                menu_user(r, login)
            else:
                new_password = input('Введите новый пароль: ')
                for i in users:
                    if i['username'] == login:
                        i['password'] = new_password
                    break
                print('Пароль изменен')
                menu_user(r, login)


def menu_admin(r):
    global rooms
    print('-----------------------------------------------------')
    print('Выберите действие:\n1. Добавление новых типов номеров\n2. Выйти\n3. Удаление типа номеров\n'
          '4. Изменение цены у типа номера\n5. Создание нового пользователя')
    print('-----------------------------------------------------')
    answer = input()
    if answer not in '12345':
        while answer not in '12345':
            answer = input('Такого действия нет! Попробуйте еще раз: ')
    match answer:
        case '1':
            new_room = input('Введите название нового типа номера: ')
            new_price = input('Введите цену нового типа номера (от 100 до 99999): ')
            while not new_price.isdigit():
                new_price = input('Ввести можно только число! ')
            new_price = int(new_price)
            while not 100 <= new_price <= 99999:
                new_price = input("Цена должна быть от 100 до 99999 "           )
                while not new_price.isdigit():
                    new_price = input("Ввести нужно число! ")
                new_price = int(new_price)
            rooms.append({'title': new_room, 'price': new_price})
            print('Добавлен новый номер!')
            menu_admin(r)
        case '2':
            start(r)
        case '3':
            room = input("Введите название номера: ")
            nomera = []
            for i in rooms:
                nomera.append(i['title'])
            while room not in nomera:
                room = input("Номера с таким названием не существует! ")
            for j in range(len(rooms) - 1):
                if room in rooms[j]['title']:
                    del rooms[j]
                    print('Тип номера удален!')
            menu_admin(r)
        case '4':
            room = input("Введите название номера: ")
            nomera = []
            for i in rooms:
                nomera.append(i['title'])
            while room not in nomera:
                room = input("Номера с таким названием не существует! ")
            new_price = input('Введите новую цену (от 100 до 99999): ')
            while not new_price.isdigit():
                new_price = input('Ввести можно только число! ')
            new_price = int(new_price)
            while not 100 <= new_price <= 99999:
                new_price = input("Цена должна быть от 100 до 99999 ")
                while not new_price.isdigit():
                    new_price = input("Ввести нужно число! ")
                new_price = int(new_price)
            for j in range(len(rooms) - 1):
                if room in rooms[j]['title']:
                    rooms[j]['price'] = new_price
                    print('Цена изменена')
            menu_admin(r)
        case '5':
            new_login = input('Введите имя пользователя: ')
            new_password = input('Введите пароль пользователя: ')
            users.append({'username': new_login, 'password': new_password, 'role': 'user', 'history': [],
                          'created_at': '2024-12-13'})
            print('Пользователь создан')
            menu_admin(r)


def start(r):
    print('Добро пожаловать на сайт Гостиницы! \nПожалуйста, авторизуйтесь. Чтобы выйти - напишите 0 в логине')
    login = input("Введите логин: ")
    if login == '0':
        print('До новых встреч!')
        return
    password = input("Введите пароль: ")
    for i in users:
        if i['username'] == login:
            if i['password'] == password:
                if i['role'] == 'admin':
                    menu_admin(r)
                    break
                else:
                    menu_user(r, login)
                    break
    print('Неверно введен пароль или логин!')
    start(r)


start(rooms)
