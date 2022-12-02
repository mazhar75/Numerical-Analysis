
import math
def calc(x,func):
    f=eval(func)
    return f
def two_segment():
    func=input()
    a=int(input())
    b=int(input())
    h=(b-a)/2
    sum=calc(a,func)
    sum+=calc(b,func)
    sum+=4*calc((a+b)/4,func)
    ans=sum*h/3
    print(ans)
def multiple_segment():
    func=input()
    a=int(input())
    b=int(input())
    n=int(input())
    h=(b-a)/n
    x=0
    y=0
    for i in range(1,n):
        if i%2==0:
            y+=calc(a+i*h,func)
        else:
          x+=calc(a+i*h,func)
    sum=calc(a,func)+4*x+2*y+calc(b,func)
    ans=(b-a)*sum/(3*n)
    print(ans)

print("choice 1 for 2-segment")
print("choice 2 for multiple segment")
while True:
    choice=int(input())
    if(choice == 1):
        two_segment()
    elif(choice == 2):
        multiple_segment()
    else :
        break