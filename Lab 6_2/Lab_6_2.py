#25. Для заданого дійсного числа x, використовуючи розкладання
#функції Arctg(x) в ряд Тейлора обчислити із заданою точністю eps значення y.
def arctg(x,eps):
    x1 = x
    x2 = (-1)*((pow(x,3))/3)
    S = x + x2
    i = 3
    while (abs(x2-x1) >= eps):
        x1 = x2
        x2 = ((-1)*x1*pow(x,2)*i)/(i+2)
        i += 2
        S += x2
    return S



x = float(input('x='))
eps = float(input('eps='))

if abs(x) < 1 :
    y = arctg(x,eps)
    print('y = %.8f' % y)
else:
    print("You've input incorrect x")



