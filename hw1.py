while True:
    try:
        a = int(input('Введите целое число для проверки: '))
    except ValueError:
        print('Некорректный ввод')
    else:
        if a < 2:
            print(a, '- не простое число')
        b = 2
        while b <= a:
            if a == b:
                print(a, '- простое число')
                break
            if a % b == 0:
                print(a, '- не простое число')
                break
            b = b + 1