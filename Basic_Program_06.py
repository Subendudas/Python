'''
@Auther: Subendu Das
@Date: 2021-11-07 10:00:30
@Last Modified by: Subendu Das
@Last Modified Time: 10:00:30
@Title: Factors -> Computes the prime factorization of N using brute force.
'''
import math
 
def primeFactors(n):
    try:

        while n % 2 == 0:
            print (2)
            n = n / 2
        for i in range(3,int(math.sqrt(n))+1,2):
            while n % i== 0:
                print (i)
                n = n / i
        if n > 2:
         print (n)
    except Exception as e:
        print(e)    
 
n = int(input("Enter number: "))
primeFactors(n)