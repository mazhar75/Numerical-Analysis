
def function(n,A,C):
    for i in range(0,n):
        for j in range(i+1,n):
            val=A[j][i]/A[i][i]
            for k in range(0,n):
                A[j][k]-=val*A[i][k]
            C[j]-=val*C[i]
    ans=[]
    for i in range(0,n):
        ans.append(0)
    ind = n-1
    while ind>=0:
        val=0
        for i in range(ind+1,n):
            val+=A[ind][i]*ans[i]
        x=C[ind]-val
        ans[ind]=x/A[ind][ind]
        ind-=1
    return ans
n=int(input("Enter the size of matrix: n*n "))
A=[]
for i in range(0,n):
    row=list(map(float,input().split()))
    A.append(row)
C=list(map(float,input().split()))
ans=function(n,A,C)
X=float(input())
Y=0
for i in range(0,n):
    Y+=ans[i]*X**i
print(Y)



