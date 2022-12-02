
n=int(input())
point=[]
for i in range(0,n):
    row=list(map(float,input().split()))
    point.append(row)
x=0
y=0
for i in range(0,n):
    x+=point[i][0]
    y+=point[i][1]
x_bar=x/n
y_bar=y/n
sum=0
squre_sum=0
for i in range(0,n):
    sum+=point[i][0]*point[i][1]
    squre_sum+=point[i][0]*point[i][0]
sum=sum*n
squre_sum=squre_sum*n
a1=(sum-x*y)/(squre_sum-x*x)
a0=y_bar-a1*x_bar
print(a0,end=" ")
print(a1)