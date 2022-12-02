

def linear():

   x0=float(input())
   y0=float(input())
   x1=float(input())
   y1=float(input())
   x=float(input())
   b0=y0
   b1=(y1-y0)/(x1-x0)
   ans=(b0+(x-x0)*b1)
   print(ans)
def quadratic():
    x0=float(input())
    y0=float(input())
    x1=float(input())
    y1=float(input())
    x2=float(input())
    y2=float(input())
    x=float(input())
    b0 = y0
    b1 = (y1 - y0) / (x1 - x0)
    b2=((y2-y1)/(x2-x1)-(y1-y0)/(x1-x0))/(x2-x0)
    ans=b0+b1*(x-x0)+b2*(x-x1)*(x-x0)
    print(ans)
def cubic():
    x0=float(input())
    y0=float(input())
    x1=float(input())
    y1=float(input())
    x2=float(input())
    y2=float(input())
    x3=float(input())
    y3=float(input())
    x=float(input())
    b0 = y0
    b1 = (y1 - y0) / (x1 - x0)
    b2 = ((y2 - y1) / (x2 - x1) - (y1 - y0) / (x1 - x0)) / (x2 - x0)
    b= ((y3 - y2) / (x3 - x2) - (y2 - y1) / (x2 - x1)) / (x3 - x1)
    b3=(b-b2)/(x3-x0)
    ans=b0+b1*(x-x0)+b2*(x-x0)*(x-x1)+b3*(x-x0)*(x-x1)*(x-x2)
    print(ans)
print("type 1-linear")
print("type 2 quadratic")
print("type 3 cubic")
while True:
    type=int(input())
    if type==1:
        linear()
    elif type==2:
        quadratic()
    elif type==3:
        cubic()
    else:
        break


