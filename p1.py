while True:
    a=int(input())
    b=int(input())
    c=int(input())
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

