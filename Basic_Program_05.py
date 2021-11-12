'''
@Auther: Subendu Das
@Date: 2021-11-07 10:00:30
@Last Modified by: Subendu Das
@Last Modified Time: 10:00:30
@Title: Harmonic Number-> Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
'''
def nthHarmonic(N):
    try:
        harmonic = 1.00
        for i in range(2, N + 1):
         harmonic += 1 / i
         return harmonic
    except:
        print(Exception)     
       
if __name__ == "__main__" :
 
    N = int(input("Enter any number: "))
    print(round(nthHarmonic(N),3))