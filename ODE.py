# ODE

import math

def calc(x, y, f):
    ff = eval(f)
    return ff

def EulerMethod():
    print('Input Initial Conditions')
    print('x(o) = ', end='')
    xo = float(input())
    print('y(o) = ', end='')
    yo = float(input())
    print('x(n) = ', end='')
    xn = float(input())
    print('h = ', end='')
    h = float(input())
    print('Input the function. For example: x^5=x**5, e^x=math.exp(x), ln(x)=math.log(x)')
    print('f(x,y) = ', end='')
    f = input()
    # total points
    n = int((xn-xo)/h)
    # preparing an array for x values
    x = []
    x.append(xo)
    for i in range(1, n+1):
        x.append(x[i-1]+h)
    # declaring an empty array for y values
    y = []
    y.append(yo) # given value
    for i in range(1, n+1):
        y.append(y[i-1]+calc(x[i-1], y[i-1], f)*h)
    print('Result, y(n) = {:.5f}'.format(y[-1]))


def HeunMethod():
    print('Input Initial Conditions')
    print('x(o) = ', end='')
    xo = float(input())
    print('y(o) = ', end='')
    yo = float(input())
    print('x(n) = ', end='')
    xn = float(input())
    print('h = ', end='')
    h = float(input())
    print('Input the function. For example: x^5=x**5, e^x=math.exp(x), ln(x)=math.log(x)')
    print('f(x,y) = ', end='')
    f = input()
    # total points
    n = int((xn - xo) / h)
    # preparing an array for x values
    x = []
    x.append(xo)
    for i in range(1, n + 1):
        x.append(x[i - 1] + h)
    a2 = 1/2
    a1 = 1-a2
    p1 = 0.5/a2
    q11 = 0.5/a2
    # declaring an empty array for y values
    y = []
    y.append(yo)  # given value
    for i in range(1, n + 1):
        k1 = calc(x[i-1], y[i-1], f)
        k2 = calc(x[i-1]+p1*h, y[i-1]+q11*k1*h, f)
        y.append(y[i - 1] + (a1*k1+a2*k2)*h)
    print('Result, y(n) = {:.5f}'.format(y[-1]))

def MidpointMethod():
    print('Input Initial Conditions')
    print('x(o) = ', end='')
    xo = float(input())
    print('y(o) = ', end='')
    yo = float(input())
    print('x(n) = ', end='')
    xn = float(input())
    print('h = ', end='')
    h = float(input())
    print('Input the function. For example: x^5=x**5, e^x=math.exp(x), ln(x)=math.log(x)')
    print('f(x,y) = ', end='')
    f = input()
    # total points
    n = int((xn - xo) / h)
    # preparing an array for x values
    x = []
    x.append(xo)
    for i in range(1, n + 1):
        x.append(x[i - 1] + h)
    a2 = 1
    a1 = 1 - a2
    p1 = 0.5 / a2
    q11 = 0.5 / a2
    # declaring an empty array for y values
    y = []
    y.append(yo)  # given value
    for i in range(1, n + 1):
        k1 = calc(x[i - 1], y[i - 1], f)
        k2 = calc(x[i - 1] + p1 * h, y[i - 1] + q11 * k1 * h, f)
        y.append(y[i - 1] + (a1 * k1 + a2 * k2) * h)
    print('Result, y(n) = {:.5f}'.format(y[-1]))

def RalstonMethod():
    print('Input Initial Conditions')
    print('x(o) = ', end='')
    xo = float(input())
    print('y(o) = ', end='')
    yo = float(input())
    print('x(n) = ', end='')
    xn = float(input())
    print('h = ', end='')
    h = float(input())
    print('Input the function. For example: x^5=x**5, e^x=math.exp(x), ln(x)=math.log(x)')
    print('f(x,y) = ', end='')
    f = input()
    # total points
    n = int((xn - xo) / h)
    # preparing an array for x values
    x = []
    x.append(xo)
    for i in range(1, n + 1):
        x.append(x[i - 1] + h)
    a2 = 2 / 3
    a1 = 1 - a2
    p1 = 0.5 / a2
    q11 = 0.5 / a2
    # declaring an empty array for y values
    y = []
    y.append(yo)  # given value
    for i in range(1, n + 1):
        k1 = calc(x[i - 1], y[i - 1], f)
        k2 = calc(x[i - 1] + p1 * h, y[i - 1] + q11 * k1 * h, f)
        y.append(y[i - 1] + (a1 * k1 + a2 * k2) * h)
    print('Result, y(n) = {:.5f}'.format(y[-1]))

def Comparison():
    print('Input Initial Conditions')
    print('x(o) = ', end='')
    xo = float(input())
    print('y(o) = ', end='')
    yo = float(input())
    print('x(n) = ', end='')
    xn = float(input())
    print('Input the function. For example: x^5=x**5, e^x=math.exp(x), ln(x)=math.log(x)')
    print('f(x,y) = ', end='')
    f = input()
    print('Exact Solution = ', end='')
    exSol = float(input())
    while True:
        print('Press 0 to exit or anything to continue')
        choice = int(input())
        if choice == 0:
            break
        print('h = ', end='')
        h = float(input())
        # total points
        n = int((xn - xo) / h)
        # preparing an array for x values
        x = []
        x.append(xo)
        for i in range(1, n + 1):
            x.append(x[i - 1] + h)
        # declaring an empty array for y values
        y = []
        y.append(yo)  # given value
        for i in range(1, n + 1):
            y.append(y[i - 1] + calc(x[i - 1], y[i - 1], f) * h)
        eulerRes = y[-1]
        # total points
        n = int((xn - xo) / h)
        # preparing an array for x values
        x = []
        x.append(xo)
        for i in range(1, n + 1):
            x.append(x[i - 1] + h)
        a2 = 1 / 2
        a1 = 1 - a2
        p1 = 0.5 / a2
        q11 = 0.5 / a2
        # declaring an empty array for y values
        y = []
        y.append(yo)  # given value
        for i in range(1, n + 1):
            k1 = calc(x[i - 1], y[i - 1], f)
            k2 = calc(x[i - 1] + p1 * h, y[i - 1] + q11 * k1 * h, f)
            y.append(y[i - 1] + (a1 * k1 + a2 * k2) * h)
        heunRes = y[-1]
        # total points
        n = int((xn - xo) / h)
        # preparing an array for x values
        x = []
        x.append(xo)
        for i in range(1, n + 1):
            x.append(x[i - 1] + h)
        a2 = 1
        a1 = 1 - a2
        p1 = 0.5 / a2
        q11 = 0.5 / a2
        # declaring an empty array for y values
        y = []
        y.append(yo)  # given value
        for i in range(1, n + 1):
            k1 = calc(x[i - 1], y[i - 1], f)
            k2 = calc(x[i - 1] + p1 * h, y[i - 1] + q11 * k1 * h, f)
            y.append(y[i - 1] + (a1 * k1 + a2 * k2) * h)
        midpointRes = y[-1]
        # total points
        n = int((xn - xo) / h)
        # preparing an array for x values
        x = []
        x.append(xo)
        for i in range(1, n + 1):
            x.append(x[i - 1] + h)
        a2 = 2 / 3
        a1 = 1 - a2
        p1 = 0.5 / a2
        q11 = 0.5 / a2
        # declaring an empty array for y values
        y = []
        y.append(yo)  # given value
        for i in range(1, n + 1):
            k1 = calc(x[i - 1], y[i - 1], f)
            k2 = calc(x[i - 1] + p1 * h, y[i - 1] + q11 * k1 * h, f)
            y.append(y[i - 1] + (a1 * k1 + a2 * k2) * h)
        ralstonRes = y[-1]
        print('Exact Solution is {:.3f}'.format(exSol))
        print('For Step Size {}, Euler: {:.2f} | Heun: {:.2f} | Midpoint: {:.2f} | Ralston: {:.2f}'.format(h,eulerRes,heunRes,midpointRes,ralstonRes))
        eErr = (abs(exSol-eulerRes)/exSol)*100
        hErr = (abs(exSol-heunRes)/exSol)*100
        mErr = (abs(exSol-midpointRes)/exSol)*100
        rErr = (abs(exSol-ralstonRes)/exSol)*100
        print('|Et|%               Euler: {:.2f} | Heun: {:.2f} | Midpoint: {:.2f} | Ralston: {:.2f}'.format(eErr,hErr,mErr,rErr))

def showMenu():
    print('-----ODE-----')
    print('0. Show Menu')
    print('1. Eulers\' Method')
    print('2. Heun\'s method')
    print('3. Midpoint method')
    print('4. Ralston\'s method')
    print('5. Comparison')
    print('6. Exit')

# Main function
showMenu()
while True:
    choice = int(input())
    if choice == 0:
        showMenu()
    elif choice == 1:
        EulerMethod()
    elif choice == 2:
        HeunMethod()
    elif choice == 3:
        MidpointMethod()
    elif choice == 4:
        RalstonMethod()
    elif choice == 5:
        Comparison()
    elif choice == 6:
        break
    else:
        print('Please enter 0 to see the menu')
