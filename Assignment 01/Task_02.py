T = int(input())
for i in range(T):
    calc = input()
    calc = calc[10:]
    if '+' in calc:
        x, y = calc.split(' + ')
        x = float(x)
        y = float(y)
        print(x+y)
    if '-' in calc:
        x, y = calc.split(' - ')
        x = float(x)
        y = float(y)
        print(x-y)
    if '/' in calc:
        x, y = calc.split(' / ')
        x = float(x)
        y = float(y)
        print(x/y)
    if '*' in calc:
        x, y = calc.split(' * ')
        x = float(x)
        y = float(y)
        print(x*y)