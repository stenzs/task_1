while True:
    a = input('Введите текст: ')
    b = ['a', 'e', 'i', 'o', 'u', 'y']
    for c in b:
        print(c, (a.lower().count(c)), '; ', end='')
    print()