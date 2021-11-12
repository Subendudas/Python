'''
@Auther: Subendu Das
@Date: 2021-11-07 09:00:30
@Last Modified by: Subendu Das
@Last Modified Time: 09:00:30
@Title: Flip Coin and print percentage of Heads and Tails.
'''
import random
Flips = int(input("How many times you want to flip the coin? "))
def flipCoin():
    '''Flipcoin function '''
    tail=0
    head=0    
    try:

        for i in range(Flips):
            f = random.random()
            if f<0.5:
                print("Tail")
                tail+=1
            else:
                print("Head")
                head+=1
    except Exception as e:
        print(e)
    print("Percentage for Head and Tail")
    resultH= (float)((head*100)/100)
    resultT= (float)((tail*100)/100)
    print("Head "+str(resultH)+"%")
    print("Tail "+str(resultT)+"%")

flipCoin()