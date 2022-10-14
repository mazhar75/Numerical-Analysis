
import matplotlib.pyplot as plt
from sympy import *

bisection_middle=[]
bisection_error=[]
false_position_middle=[]
false_position_error=[]
newton_raphson_middle=[]
newton_raphson_error=[]
secant_middle=[]
secant_error=[]
"""
Here 8 list for 4 methods.
Every methods has two lists with its name.

middle-> store middle point in every iteration.
error-> store absulate relative approximate error.

""" 

def bisection_method(func,a,b,tolerable_error):
   """
   This function finding root base of bijection method.
   ------------------
   parameter list:
   func: Function in which we wants to find root.
   a:lower limit
   b:upper limit
   tolerable_error: indicate that how much error accepted.
   ------------------
   f(x): calculate the func value depends on x.
   fun(x): calculate the value next guess.
   """
   print("Using Bisection method on:"+func)
   try:
    def f(x):
      f = eval(func)
      return f
   except Exception as e:
     print(e)
   found = True  
   if(f(a)*f(b)>0):
     print("There has no root in ",a," to ",b," limit .")
     found = False
   elif f(a)*f(b)==0:
     if(f(a)==0):
       print("The root is :",a)
     else:
       print("The root is :",b)
     found = False  
   itr=1
   if(found):
     print("Iteration  "+"  xl  "+"  xu  "+"  xm  "+"   f(xm)  ")
     print("--------------------------------------------------")       
   while found:
     mid = (a+b)/2
     if(itr==1):
       bisection_middle.append(mid)
       bisection_error.append(0)
       error=0
       print(itr," ",a," ",b," ",mid," ",error," ",f(mid))
     else :
       prev=bisection_middle.pop()
       error=abs((mid-prev)/mid)*100
       bisection_error.append(error)
       bisection_middle.append(prev)
       bisection_middle.append(mid)
       print(itr," ",a," ",b," ",mid," ",error," ",f(mid))
     if(itr>1 and abs(bisection_error[-1]/100)<tolerable_error):
       found=False
         
     elif f(a)*f(mid)<0:
       b=mid
     else:
       a=mid
     itr+=1  
   print("-------------------------------------------------------")
   if(itr>1):
     print("Expected root :",mid)
   list1=[]
   l=len(bisection_error)
   print("Total iteration by bisection method :",l)
   for i in range(0,l):
     list1.append(i+1)
   plt.plot(list1,bisection_error) 
   plt.xlabel("iteration")
   plt.ylabel("error")
   plt.title("Iteration vs error graph by bisection method:") 


def false_position_method(func,a,b,tolerable_error):
   """
   This function finding root base of false position method.
   ------------------
   parameter list:
   func: Function in which we wants to find root.
   a:lower limit
   b:upper limit
   tolerable_error: indicate that how much error accepted.
   ------------------
   f(x): calculate the func value depends on x.
   """
   print("Using False position method on :"+func)
   try:
    def f(x):
      f = eval(func)
      return f
   except Exception as e:
     print(e)
   try:     
    def fun(x,y):
      point=(y*f(x)-x*f(y))/(f(x)-f(y))
      return point
   except Exception as e:
     print(e)   

   
   found = True  
   if(f(a)*f(b)>0):
     print("There has no root in ",a," to ",b," limit .")
     found = False
   elif f(a)*f(b)==0:
     if(f(a)==0):
       print("The root is :",a)
     else:
       print("The root is :",b)
     found = False  
   itr=1
   if(found):
     print("Iteration  "+"  xl  "+"  xu  "+"  xm  "+"   f(xm)  ")
     print("--------------------------------------------------")       
   while found:
     mid = fun(a,b)
     if(itr==1):
       false_position_middle.append(mid)
       false_position_error.append(0)
       error=0
       print(itr," ",a," ",b," ",mid," ",error," ",f(mid))
     else :
       prev=false_position_middle.pop()
       error=abs((mid-prev)/mid)*100
       false_position_error.append(error)
       false_position_middle.append(prev)
       false_position_middle.append(mid)
       print(itr," ",a," ",b," ",mid," ",error," ",f(mid))
     if(itr>1 and abs(false_position_error[-1]/100)<tolerable_error):
       found = False
         
     elif f(a)*f(mid)<0:
       b=mid
     else:
       a=mid
     itr+=1  
   print("--------------------------------------------------------")
   if(itr>1):
     print("Expected root :",mid)
   l=len(false_position_error)
   list2=[]
   print("Total iteration by false position method :",l)
   for i in range(0,l):
     list2.append(i+1)
   plt.plot(list2,false_position_error) 
   plt.xlabel("iteration")
   plt.ylabel("error")
   plt.title("Iteration vs error graph by false position method:")  


def newton_raphson_method(func,x,tolarable_error):
   """
   This function finding root base of Newton Raphson method.
   ------------------
   parameter list:
   func: Function in which we wants to find root.
   x=initial guess.
   tolerable_error: indicate that how much error accepted.
   ------------------
   f(x): calculate the func value depends on x.
   fun(x): calculate the value next guess.
   """
   print("Using Newton Raphson method on:"+func) 
   need = []
   try:
     def f(x):
       f=eval(func)
       return f
   except Exception as e:
      print(e) 
   try:
     def derivative(val,cnt):  
       
       x = symbols('x')
       if cnt>1:
         newfun=need.pop()
         df=diff(newfun,x)
         need.append(df)
         z = df.subs(x, val).evalf()
         y=val-f(val)/z
         return y
       else:  
         df=diff(func,x)
         need.append(df)
         z = df.subs(x, val).evalf()
         y=val-f(val)/z
         return y
         
   except Exception as e:
     print(e)
   found = True
 
   if(f(x)==0):
     print("The root is : ",x)
     found = False
   if(found):
     print("Iteration  |  Guess  |   Error  ")
     print("--------------------------------")
   itr=1  
   while found:
     if(itr==1):
       newton_raphson_error.append(0)
       newton_raphson_middle.append(x)
       print(itr,"  ",x,"  ",0)
     else :
       prev=newton_raphson_middle.pop()
       error=abs((x-prev)/x)*100
       newton_raphson_error.append(error)
       newton_raphson_middle.append(prev)
       newton_raphson_middle.append(x)
       print(itr,"  ",x,"  ",error)
     if(itr>1 and abs(newton_raphson_error[-1]/100)<tolarable_error):
       found = False
       itr+=1
     else:
       x=derivative(x,itr)
       
       itr+=1 
      
   if(itr>1):
    print("----------------------------------")
    print("Expected root : ",x)
   l=len(newton_raphson_error)
   list3=[]
   print("Total iteration by newton raphson method :",l)
   for i in range(0,l):
     list3.append(i+1)
   plt.plot(list3,newton_raphson_error) 
   plt.xlabel("iteration")
   plt.ylabel("error")
   plt.title("Iteration vs error graph by newton raphson method:") 



def secant_method(func,x,y,tolerable_error):
   """
   This function finding root base of secant method.
   ------------------
   parameter list:
   func: Function in which we wants to find root.
   x=initial guess.
   tolerable_error: indicate that how much error accepted.
   ------------------
   f(x): calculate the func value depends on x.
   fun(x): calculate the value next guess.
   """
   print("Using secant method on:"+func) 
   need = []
   try:
     def f(x):
       f=eval(func)
       return f
   except Exception as e:
      print(e) 
   
   found = True
 
   if(f(x)==0):
     print("The root is : ",x)
     found = False
   elif(f(y)==0):
     print("The root is : ",y)
     found = False  
   if(found):
     print("Iteration  |  lower bound  | upper bound | Guess |  Error  ")
     print("-----------------------------------------------------------")
   itr=1  
   need.append(x)
   need.append(y)
   while found:
     x=need.pop()
     y=need.pop()
     val=y-(f(y)*(y-x))/(f(y)-f(x))
     need.append(y)
     need.append(val)
     if(itr==1):
       secant_middle.append(val)
       secant_error.append(0)
       print(itr,"  ",x,"  ",y,"  ",val,"  ","----")
     else:
       prev=secant_middle.pop()
       error=abs((val-prev)/val)*100
       secant_error.append(error)
       secant_middle.append(prev)
       secant_middle.append(val)
       print(itr,"  ",x,"  ",y,"  ",val,"  ",error)
     if(itr>1 and secant_error[-1]<tolerable_error):
       found=False
     itr+=1


      
   if(itr>1):
    print("--------------------------------------------------------")
    print("Expected root : ",x)
   l=len(secant_error)
   list4=[]
   print("Total iteration by false position method :",l)
   for i in range(0,l):
     list4.append(i+1)
   plt.plot(list4,secant_error) 
   plt.xlabel("iteration")
   plt.ylabel("error")
   plt.title("Iteration vs error graph by secant method:")   



print("Assalamualaikum ")
print("This code by Md.Mazharul Islam")
print("Note : You need to matplotlib and sympy module for graph.")
print("Which method would you prefer for root finding ?")
print("click 1 for Bisection method ")
print("click 2 for False Position method ")
print("click 3 for Newton Raphson method ")
print("click 4 for Secant method ")
option=int(input())
f=input("Enter the function :")
if option ==1 :
  
  low=float(input("Enter lower bound :"))
  high=float(input("Enter Upper bound :"))
  error=float(input("Enter Tolerable Error:"))
  bisection_method(f,low,high,error)
elif option==2:
  
  low=float(input("Enter lower bound :"))
  high=float(input("Enter Upper bound :"))
  error=float(input("Enter Tolerable Error:"))
  false_position_method(f,low,high,error)
elif option==3:
  high=float(input("Enter initial guess :"))
  error=float(input("Enter Tolerable Error:"))
  newton_raphson_method(f,high,error)
elif option==4:
  low=float(input("Enter first initial guess :"))
  high=float(input("Enter second initial guess :"))
  error=float(input("Enter Tolerable Error:"))
  secant_method(f,low,high,error)
else :
  print("You enter wrong option.Try again !")  






  