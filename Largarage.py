
n=int(input())
a=[]
for i in range(n):
    row=list(map(float,input().split()))
    a.append(row)
x=float(input())
ans=0
for i in range(n):
    val=1.0
    for j in range(n):
        if i != j:
           val*=((x-a[j][0])/(a[i][0]-a[j][0]))

    val*=a[i][1]
    ans+=val
print(ans)