while True:
    try:
        a = float(input('Введите число для  расчета: '))
    except ValueError:
        print('Некорректный ввод')
    else:
        while True:
            b = input('Введите действие (+x; -x; *x; /x; **x; =): ')
            if b[0] == '=':
                break
            while True:
                try:
                    c = float(b[1:])
                except ValueError:
                    try:
                        c = float(b[2:])
                    except ValueError:
                        print('Некорректный ввод, продолжайте вычисления')
                        break
                    else:
                        if b[0:2] == '**':
                            c = float(b[2:])
                            a = (a ** c)
                            print('Промежутчный результат: ', a)
                            break
                        else:
                            print('Некорректный ввод, продолжайте вычисления')
                            break
                else:
                    if b[0] == '+':
                        a = (a + c)
                        print('Промежутчный результат: ', a)
                        break
                    if b[0] == '-':
                        a = (a - c)
                        print('Промежутчный результат: ', a)
                        break
                    if b[0] == '*':
                        a = (a * c)
                        print('Промежутчный результат: ', a)
                        break
                    if b[0] == '/':
                        if c != 0:
                            a = (a / c)
                            print('Промежутчный результат: ', a)
                            break
                        else:
                            print('Деление на ноль невозможно, продолжайте вычисления')
                            break
                    else:
                        print('Некорректный ввод, продолжайте вычисления')
                        break
        print('Ответ:', a)
        exit()