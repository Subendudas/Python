'''
@Auther: Subendu Das
@Date: 2021-11-11 08:00:03
@Last Modified by: Subendu Das
@Last Modified Time: 08:00:03
@Title: Quadratic Equation
a. Desc -> This program takes input and check the roots of a Quadratic equation.
'''
# Python program to find roots of quadratic equation
import math
#User input
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

'''function for finding roots'''
def equationroots( a, b, c):
    delta = b*b-4*a*c
    sqrt_val = math.sqrt(abs(delta))
    print('delta value = ',delta)
    print('sqrt value = ',sqrt_val)
    if delta>0:
        #print("Real and Different Roots")
        try:
            print((-b+sqrt_val)/(2*a))
            print((-b-sqrt_val)/(2*a))
            print("Real and Different Roots")
        except ZeroDivisionError:
                #print(Exception)
                print("Cannot divide by zero")        
    elif delta==0:
        print("Real and Same roots")
        try:
            print(-b/2*a)
        except ZeroDivisionError:
            print("Cannot Divide by zero.")
    else:
        print("Complex Roots.")
        print(-b / (2 * a), " + i", sqrt_val)
        print(- b / (2 * a), " - i", sqrt_val)
   
equationroots(a,b,c)        