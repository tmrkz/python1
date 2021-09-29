while True:
    a=(input())
    b=(input())
    c=(input())
    if type(a)==str:
        print('неверный тип переменной a!!!')
        break
    if type(b)==str:
        print('неверный тип переменной b!!!')
        break
    if type(c)==str:
        print('неверный тип переменной c!!!')
        break
    D=b * b - 4 * a * c
    if D>0:
        x1= (-b+(D)**0.5)/2*a
        x2= (-b-(D)**0.5)/2*a
        print(x1,' ',x2)
    elif D==0:
        x= (-b)/2*a
        print(x)
    else:
        print('Нет корней!')

