
import math
def calc(x,func):
    f=eval(func)
    return f
def singlesegment():
	print('Enter the function:', end='') # update
	func=input()
	print('Enter the value of a:', end='') # update
	a=int(input())
	print('Enter the value of b:', end='') # update
	b=int(input())
	ans=(b+a)*(calc(a,func)+calc(b,func))/2
	print(ans)
def multiplesegment():
	print('Enter the function:', end='') # update
	func=input()
	print('Enter the value of a:', end='') # update
	a=int(input())
	print('Enter the value of b:', end='') # update
	b=int(input())
	print('Enter the value of n:', end='') # update
	n=int(input())
	h=(b-a)/n
	sum=0
	for i in range(1,n):
		sum+=calc(a+i*h,func)
	sum*=2
	sum+=(calc(a,func))+calc(b,func)
	ans=(b-a)*sum/(2*n)
	print(ans)
print("Choice 1 for single segment")
print("Choice 2 for multiple segment")

while True:
	print('Enter your choice:', end='') # update
	choice = int(input())
	if(choice == 1):
		singlesegment()
	elif(choice == 2):
		multiplesegment()
	else:
		break